from PO.Public import login_by_sms

if __name__ == '__main__':
    page = login_by_sms.LoginBySMS()
    print(page.get_sms_code())



