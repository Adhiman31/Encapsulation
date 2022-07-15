import logging
logging.basicConfig(filename ="enc.log",level=logging.DEBUG ,format="%(levelname)s %(asctime)s %(message)s")

class ineuron :

    def __init__(self):
        self.__fees = 10000

    def disp_fees(self):
        try:
            logging.info("the fees is %s : " ,self.__fees)
        except Exception as e:
            logging.error(e)

    def set_fee(self,updated_fee):
        try:
            self.__fees = updated_fee
        except Exception as e:
            logging.error(e)


i = ineuron()
logging.info("ineuron class object created")
logging.info(i.disp_fees())


logging.info("trying to change the fees")
i.__fee = 15000
logging.info(i.disp_fees())

logging.info("calling setter method")
logging.info(i.set_fee(15000))
logging.info("Now checking the updated fee")
logging.info(i.disp_fees())

logging.info("We cannot change the private varibale value outside the class ,we can change it only within the class , inside the class methods")

