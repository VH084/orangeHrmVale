def test_case_9_employee_management_table_verification(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.wait_for_table()
    a = app.orangeHrm.employeeManagement.table.get_column_data('employee_id')
    b = app.orangeHrm.employeeManagement.table.get_column_data('employee_name')
    c = app.orangeHrm.employeeManagement.table.get_column_data('employee_job_title')
    d = app.orangeHrm.employeeManagement.table.get_column_data('employment_status')
    app.assert_that(app.orangeHrm.employeeManagement.table[1]['employee_id']).is_equal_to('1061')
    app.assert_that(app.orangeHrm.employeeManagement.table[0]['employee_name']).is_equal_to('Mazie Abraham')
    app.assert_that(app.orangeHrm.employeeManagement.table[4]['employment_status']).is_equal_to('Full-Time Permanent')

    print(a, b, c, d)


    ## 1 Create a new object of the table class inside the employee management component (based on the example from hr_administration).
    ## 2 Find selectors: For list of rows and list of column elements (Employee Id, Name, Job Title, Employment Status).
    # 3 Get list of elements from each defined column and assert them with the expected one.
    # 4 Get second element from the 'Employee Id' column and assert it with the expected one.
    # 5 Get first element from the 'Name' column and assert it with the expected one.
    # 6 Get fifth element from the 'Employment Status' column and assert it with the expected one.
