import sys
from flask import Flask
from mushrooms.logger import logging
from mushrooms.exception import MushroomsException
app=Flask(__name__)


@app.route("/",methods=['GET','POST'])
def index():
    try:
        raise Exception("We are testing custom exception")
    except Exception as e:
        mushrooms = MushroomsException(e,sys)
        logging.info(mushrooms.error_messages)
        logging.info("We are testing logging module")
    return "CI CD pipeline has been established."


if __name__=="__main__":
    app.run(debug=True)