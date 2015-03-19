import gspread

# Login with your Google account
gc = gspread.login('feedmebot@gmail.com', 'r33ek3h05')

# Open a worksheet from spreadsheet with one shot
wks = gc.open_by_url('https://docs.google.com/spreadsheets/d/1IZXCTvr-ZgR0A4uNFIcCrJBk4EnjSW4x6bgU9R9kR4s/edit').sheet1

wks.update_cell(1, 2, "it's down there somewhere, let me take another look.")
