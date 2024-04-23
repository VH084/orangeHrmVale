
from fixture.step import StepHelper
from selenium.webdriver.remote.webdriver import WebDriver

from fixture.table import Table


class EmployeeManagement:
    home_button = "a[data-automation-id='menu_home']"
    list_of_widgets_header_texts = ".widget-header span:last-child"
    employee_first_table_row = '#employeeListTable tbody tr'
    employee_filter_users_button = '*[data-tooltip="Filter"]'

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd

    def click_home(self):
        self.step.click_on_element(self.home_button)

    def get_widgets_headers(self):
        return self.step.get_elements_texts(self.list_of_widgets_header_texts)

    def __init__(self, step: StepHelper, wd: WebDriver):
        self.step = step
        self.wd = wd
        self.table = Table(step,
                           row_selector='#employeeListTable tbody tr',
                           column_selectors={'user_icon': 'td:nth-child(1)',
                                             'employee_id': 'td:nth-child(2)',
                                             'employee_name': 'td:nth-child(3)',
                                             'employee_job_title': 'td:nth-child(4)',
                                             'employment_status': 'td:nth-child(5)',
                                             'sub_unit': 'td:nth-child(6)',
                                             'cost_center': 'td:nth-child(7)',
                                             'location': 'td:nth-child(8)',
                                             'supervisor': 'td:nth-child(9)'})

    def wait_for_table(self):
        self.step.wait_for_element(self.employee_first_table_row, 40)

    def click_on_employee_filter(self):
        self.step.click_on_element(self.employee_filter_users_button, 1)
