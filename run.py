from booking.booking import Booking

with Booking() as bok:
    bok.land_first_page()
    bok.change_currency(currency='USD')
    bok.select_place_to_go('New York')
    bok.select_dates(check_in_date='2021-09-23',
                     check_out_date='2021-09-25')
    bok.select_adults(1)
    bok.click_search()

