def test_case_11_add_course_verify_coordinator(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.orangeHrm.sideMenu.click_on_side_menu_button('Training')
    app.orangeHrm.training.wait_for_page_loading()
    app.orangeHrm.training.click_on_filter_button()
    app.orangeHrm.popUp.training_filter.set




