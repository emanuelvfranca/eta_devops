
class Test1:

    def test_mandatory_fields_contact_us(self, open_contact_us):
        self.contact_us = open_contact_us
        assert self.contact_us.is_contact_us_page(), "Contact Us page is not opened"

        self.contact_us.send_message()
        assert self.contact_us.get_alert_message() == "Invalid email address.", \
            "Correct message error was not displayed"

        self.contact_us.fill_email("evfgs@cesar.school")
        self.contact_us.send_message()
        assert self.contact_us.get_alert_message() == "The message cannot be blank.", \
            "Correct message error was not displayed"

        self.contact_us.fill_message("Hey, I did not liked the server response of this site "
                                     "when multiple access are being done")
        self.contact_us.send_message()
        assert self.contact_us.get_alert_message() == "Please select a subject from the list provided.", \
            "Correct message error was not displayed"

        self.contact_us.select_heading("Webmaster")
        self.contact_us.send_message()
        assert self.contact_us.get_alert_message() == "Your message has been successfully sent to our team.", \
            "Correct message error was not displayed"
