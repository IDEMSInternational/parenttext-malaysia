sources = [
    {"filename": "parenttext_onboarding", "spreadsheet_id": "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I", "crowdin_name": "onboarding", "split_no": 2},
]

#Data copied from Chiara's pipeline for testing on multiple files

# sources = [
#     {"filename": "parenttext_onboarding", "spreadsheet_id": "12ddvTz_ZfC-9-b0yxjVrSzczciUUE3GosLUFeOLIv9I", "crowdin_name": "onboarding"},
#     {"filename": "parenttext_modules", "spreadsheet_id": "1ONmD9PF9rcno3ha3QpfrIR5EIvHuuEqJXF3T90rlZ78", "crowdin_name": "modules_teen"},
#     {"filename": "parenttext_goalcheckin", "spreadsheet_id": "1gympuD5KdlAdDJSuaVQiXjWSwJxoDcA9K-oBRyKmS7o", "crowdin_name": "goal_checkins"},
#     {"filename": "parenttext_dev_assess_tools", "spreadsheet_id": "1OhhQF5yarUDmaSl2tlt7eIT7wJ8bGwNFzI3BOplJYsc", "crowdin_name": "dev_assess_tools"},
#     {"filename": "parenttext_ltp_act_teen", "spreadsheet_id": "1Jx7vOmdefzK62ao2nlJJVLMAIS8d-6r1G8qn0jG8gww", "crowdin_name": "ltp_activities_teen"}
# ]

model = "models.parenttext_models"
languages = [
    {"language": "swa", "code": "ss"}
]

translation_repo = "../PLH-Digital-Content/translations/parent_text_v2"
outputpath = "./output"
select_phrases = "./edits/select_phrases.json"
add_selectors = "yes"
special_words = "./edits/special_words.json"
ab_testing_sheet_ID = "1i_oqiJYkeoMsYdeFOcKlvvjnNCEdQnZlsm17fgNvK0s"
dict_edits_sheet_ID = None
SG_sheet_ID = None
SG_flow_name = None
SG_path = None