# API Constants - class which contain all the endpoints
# keep all the urls
class APIConstants(object):

    @staticmethod
    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    # static method -> which can be called by without object directly by class can call it.

    @staticmethod
    def url_create_booking(self):
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token(self):
        return "https://restful-booker.herokuapp.com/auth"

    @staticmethod
    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

    @staticmethod
    def url_get_booking(booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)

