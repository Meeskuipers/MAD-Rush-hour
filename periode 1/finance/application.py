"""
Mees Kuipers
11288477

This program runs a website. This website is connected to the stack market.
You can register and it will be saved in the database. when this is done
you get a start capital of 10000 dollars. Next time you can log in and buy
some stocks of a company. When the stocks have a good value you can sell them
again, hopefully with some provid. It is also possible to see the history that
was bought and sold.
"""

import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Ensure environment variable is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/", methods=["GET", "POST"])
@login_required
def index():
    """Show portfolio of stocks"""
    # This index keeps track of every stock that is owned
    index = []
    # This is needed to itterate over every stock that is owned
    lenght = len(db.execute("SELECT * FROM personal WHERE id_person = :id", id=session["user_id"]))
    all_of_list = db.execute("SELECT * FROM personal WHERE id_person = :id", id=session["user_id"])
    # The cash that is owned by the user
    cash = db.execute("SELECT * FROM users WHERE id = :id", id=session["user_id"])[0]['cash']
    total_sum = 0

    # In this loop all the information is gatherd to put in the index. After this
    # the information is send to index.html
    for i in range(lenght):
        symbol = all_of_list[i].get('company')
        dictio = lookup(symbol)
        if not dictio:
            return apology("lookup doesnt work")
        name = dictio['name']
        stacks = all_of_list[i].get('stacks')
        current_price = dictio['price']
        total = stacks * current_price
        list_company = [symbol, name, stacks, usd(current_price), usd(total)]
        index.append(list_company)
        total_sum += total
    grand_total = total_sum + cash
    winst = grand_total - 10000
    return render_template("index.html", table=index, cash=usd(cash), grand_total=usd(grand_total), winst=usd(winst))


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    # If the button on is clicked this if statement is true
    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        # Checks if the inputed value is not none
        if not shares:
            return apology("put in a number of shares")
        # If it is none an interture can bet taken
        shares = int(shares)
        quote = lookup(symbol)
        # Checks if quot is not none
        if not quote:
            return apology("Symbol does not excist", 400)

        # Ensure that the amount of shares is higher then 0
        elif shares < 1:
            return apology("must provide number of shares correctly", 400)

        users_cash = db.execute("SELECT * FROM users WHERE id = :id",
                                id=session["user_id"])[0]['cash']

        total_bought = (quote["price"] * shares)

        # If the user has not enough money the payement will stop
        if users_cash < total_bought:
            return apology("You don't have enough money")

        # The cash of the user will be less if he has bought stocks
        db.execute("UPDATE users SET cash = cash - :min WHERE id = :id",
                   min=total_bought, id=session["user_id"])

        # The personal table in the database keep track of every stock he own
        # of a specific company. There will be never two different payement of
        # the same company, this check makes sure of this
        check = db.execute("SELECT * FROM personal WHERE id_person = :id AND company = :c", id=session["user_id"], c=symbol)

        # Aankoop is used to print every payement that is done
        db.execute("INSERT INTO aankoop (stack,money,afkorting,company,id_player) VALUES (:s, :m, :a, :c, :id)",
                   s=shares, m=quote["price"] * shares, a=symbol, c=lookup(symbol)["name"], id=session["user_id"])

        # if the user already had stocks of the company this stocks will be update
        # otherwise there will be inserted a new row in the table
        if check:
            users_stacks = int(db.execute("SELECT * FROM personal WHERE id_person = :id AND company = :symbol",
                                          id=session["user_id"], symbol=symbol)[0]['stacks'] + shares)

            db.execute("UPDATE personal SET stacks = :stacks WHERE id_person = :id AND company = :symbol",
                       stacks=users_stacks, id=session["user_id"], symbol=symbol)
        else:
            db.execute("INSERT INTO personal (id_person,company,stacks) VALUES (:id, :c, :s)",
                       id=session["user_id"], c=symbol, s=shares)
        return redirect("/")
    # If the no buttom is clicked the website will go to buy.html
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""

    # Is almost the same as index. The values are only different and all the
    # values of aankoop are itterated
    index = []
    lenght = len(db.execute("SELECT * FROM aankoop"))
    all_of_list = db.execute("SELECT * FROM aankoop")

    for i in range(lenght):
        symbol = all_of_list[i].get('company')
        stacks = all_of_list[i].get('stack')
        current_price = all_of_list[i].get('money')
        time = all_of_list[i].get('time_date')
        aankoop = [symbol, stacks, current_price, time]
        index.append(aankoop)

    return render_template("history.html", table=index)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 400)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # The post thing is the same as by buy
    if request.method == "POST":
        # Checks if there is a proper input
        if not request.form.get("symbol"):
            return apology("Invalid symbol", 400)
        quote = lookup(request.form.get("symbol"))
        if not quote:
            return apology("Symbol does not excist", 400)
        # Makes a list of everyting that is neede to be print in quote.html
        list_quote = [quote["name"], quote["symbol"], usd(quote["price"])]
        return render_template("quotes.html", quote=list_quote)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure both passwords are equals
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords are not equal", 400)

        result = db.execute("SELECT * FROM users WHERE username = :username",
                            username=request.form.get("username"))
        if result:
            return apology("Username already excist", 400)

        # Query database for username
        rows = db.execute("INSERT INTO users (username,hash) VALUES (:u, :h)",
                          u=request.form.get("username"), h=generate_password_hash(request.form.get("password")))

        # Remember which user has logged in
        session["user_id"] = rows

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    # is exactly the same as buy, only the other way around
    company_list = []
    if request.method == "POST":

        shares = int(request.form.get("shares"))
        company = request.form.get("symbol")
        amount_shares = db.execute("SELECT * FROM personal WHERE id_person = :id",
                                   id=session["user_id"])[0]['stacks']

        if shares > amount_shares:
            return apology("you don't have that amount of shares")
        shares = amount_shares - shares
        if shares == 0:
            db.execute("DELETE * FROM personal WHERE id_person = :id AND company = :company;",
                       id=session["user_id"], company=company)
        else:
            db.execute("UPDATE personal SET stacks = :stacks WHERE id_person = :id",
                       stacks=shares, id=session["user_id"])
        quote = lookup(company)
        print(quote)
        if not quote:
            return apology("lookup doesnt work", 400)
        db.execute("INSERT INTO aankoop (stack,money,afkorting,company,id_player) VALUES (:s, :m, :a, :c, :id)",
                   s=request.form.get("shares"), m=-quote["price"] * shares, a=company, c=quote["name"], id=session["user_id"])

        plus = quote["price"] * shares
        db.execute("UPDATE users SET cash = cash + :plus WHERE id = :id",
                   plus=plus, id=session["user_id"])

        return redirect("/")
    else:
        # lenght and all_of_list is used to itterate over everyting that is bought
        # This will be returnd to sell.html. This file use these information
        # to make a dropdown menu
        lenght = len(db.execute("SELECT * FROM personal WHERE id_person = :id", id=session["user_id"]))
        all_of_list = db.execute("SELECT * FROM personal WHERE id_person = :id", id=session["user_id"])
        for i in range(lenght):
            symbol = all_of_list[i].get('company')
            company_list.append(symbol)
        return render_template("sell.html", company_list=company_list)


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
