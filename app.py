from flask import Flask, request
from random import choice, sample

app = Flask(__name__)

horoscope = {
    'Aries':"your lame af",
    'Taurus':"you the bullyest",
    'Gemini':"You have a twin somewhere... Find them",
    'Cancer':"Are you feeling it mister crabs",
    'Leo':"Go find your zebra you lion",
    'Virgo':"You are not just but a maiden but a mighty god find yourself and rule your life",
    'Libra':"Judgment Shall be passed on those that Judge others",
    'Scorpio':"You shall sting all your relationships and fail in life",
    'Sagittarius':"The Centaurus Archer The Best Makersman In all History",
    'Capricorn': "Your a horny mountain goat forever trapped on a floating spike",
    'Aquarius': "The bearer of plenty shall be hold you soon",
    'Pisces': "Theres plenty of fish in the see"
}

@app.route('/')
def index():
    """Show the homepage and ask the user's name."""
    return """
    <form action='/horoscope'>
        <p>
            What is your Horoscope sign: 
            <input type="text" name="horoscope"/>
        </p>
        <p>
            <input type="checkbox" name="show_horoscope"/>
            Show horoscope
        <input type="submit">
        <select name="num_compliments">
            <option value="1">One</option>
            <option value="2">Two</option>
            <option value="3">Three</option>
    </select>
    </form>
    """

@app.route('/horoscope')
def get_horoscope():
    """Give the user a daily horoscope"""
    sign = request.args.get('horoscope')
    show_horoscope = request.args.get('show_horoscope')
    nice_things = horoscope[sign]
    #nice_things = ', '.join(sample(horoscopes, num_compliments))

    if show_horoscope:
        return f'Hello there, {sign}! Your Horoscope today is:  {nice_things}!'
    else:
        return f'Hello there, {sign}! Have a nice day!'

if __name__ == "__main__":
   app.run(debug=True)
