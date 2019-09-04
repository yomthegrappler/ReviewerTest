import pytest
from Utility.constant import Constant
from Utility.excel_mgmt import ExcelExec
from Utility.module_mapping import DriverMapping

@pytest.mark.usefixtures("setup")
class TestMainExec:

    @pytest.fixture(autouse=True)
    def initial_setup(self, setup):
        self.constant = Constant()
        self.excel = ExcelExec()
        self.driver_method = DriverMapping(self.driver)

    @pytest.mark.run(order=1)
    def test_main(self):
        self.execute_test_main()

    def execute_test_main(self):
        test_module_max_row = self.excel.get_row_count(self.constant.Sheetname_Module) + 1
        test_collection_max_row = self.excel.get_row_count(self.constant.Sheetname_Scenario) + 1

        for fromTestModuleRow in range(2, test_module_max_row):

            test_module_id_val_1 = self.excel.get_cell_data(
                self.constant.Sheetname_Module,
                fromTestModuleRow,
                self.constant.Test_Module_ID_Col_1
            )

            test_module_name_val_1 = self.excel.get_cell_data(
                self.constant.Sheetname_Module,
                fromTestModuleRow,
                self.constant.Test_Module_Name_Col_1
            )

            run_mode_val_1 = self.excel.get_cell_data(
                self.constant.Sheetname_Module,
                fromTestModuleRow,
                self.constant.Test_Mod_RunMode_Col
            )

            if str(run_mode_val_1).upper() == "SKIP":
                continue

            if str(run_mode_val_1).upper() == "YES":
                test_module_max_row = self.excel.get_row_count(test_module_name_val_1)
                if test_module_max_row is None or test_module_max_row is False:
                    continue

            for fromTestCollectionRow in range(2, test_collection_max_row):
                test_module_id_val_2 = self.excel.get_cell_data(
                    self.constant.Sheetname_Scenario,
                    fromTestCollectionRow,
                    self.constant.Test_Module_ID_Col_2
                )

                if test_module_id_val_1 == test_module_id_val_2:
                    test_module_name_val_2 = self.excel.get_cell_data(
                        self.constant.Sheetname_Scenario,
                        fromTestCollectionRow,
                        self.constant.Test_Module_Name_Col_2
                    )

                    test_case_id_val_1 = self.excel.get_cell_data(
                        self.constant.Sheetname_Scenario,
                        fromTestCollectionRow,
                        self.constant.Test_Case_ID_Col_1
                    )

                    test_case_name_val = self.excel.get_cell_data(
                        self.constant.Sheetname_Scenario,
                        fromTestCollectionRow,
                        self.constant.Test_Case_Name_Col
                    )

                    run_mode_val_2 = self.excel.get_cell_data(
                        self.constant.Sheetname_Scenario,
                        fromTestModuleRow,
                        self.constant.Test_Scen_RunMod_Col
                    )

                    if str(run_mode_val_2).upper() == "SKIP":
                        continue

                    if str(run_mode_val_2).upper() == "YES":
                        test_case_id = test_case_id_val_1

                        for fromTestStepRow in range(2, test_module_max_row + 1):
                            test_case_id_val_2 = self.excel.get_cell_data(
                                test_module_name_val_1,
                                fromTestStepRow,
                                self.constant.Test_Case_ID_Col_2
                            )

                            if test_case_id == test_case_id_val_2:

                                test_step_id = self.excel.get_cell_data(
                                    test_module_name_val_1,
                                    fromTestStepRow,
                                    self.constant.Test_Step_ID_Col
                                )

                                test_step_description = self.excel.get_cell_data(
                                    test_module_name_val_1,
                                    fromTestStepRow,
                                    self.constant.Test_Step_Desc_Col
                                )

                                action_keyword = self.excel.get_cell_data(
                                    test_module_name_val_1,
                                    fromTestStepRow,
                                    self.constant.Test_Step_ActionKey_Col
                                )

                                step_property = self.excel.get_cell_data(
                                    test_module_name_val_1,
                                    fromTestStepRow,
                                    self.constant.Test_Step_Property_Col
                                )

                                nObject = self.excel.get_cell_data(
                                    test_module_name_val_1,
                                    fromTestStepRow,
                                    self.constant.Test_Step_Object_Col
                                )

                                nObject_value = self.excel.get_object_value(
                                    self.constant.Sheetname_Objects,
                                    nObject
                                )

                                nData_value = self.excel.get_cell_data(
                                    test_module_name_val_1,
                                    fromTestStepRow,
                                    self.constant.Test_Step_Value_Col
                                )

                                stepResult = self.driver_method.execute_keyword(
                                    action_keyword,
                                    nData_value,
                                    nObject_value
                                )


























