# -*- coding: utf-8 -*-
# Copyright 2019 OpenSynergy Indonesia
# Copyright 2021 PT. Simetri Sinergi Indonesia
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).
{
    "name": "Loan Management",
    "version": "8.0.2.2.2",
    "category": "Loan & Saving",
    "website": "https://simetri-sinergi.id",
    "author": "OpenSynergy Indonesia, PT. Simetri Sinergi Indonesia",
    "license": "LGPL-3",
    "application": True,
    "installable": True,
    "depends": [
        "account_accountant",
        "base_action_rule",
        "loan_saving_core",
        "base_sequence_configurator",
        "base_workflow_policy",
        "base_cancel_reason",
        "base_multiple_approval",
        "web_readonly_bypass",
    ],
    "data": [
        "security/ir.model.access.csv",
        "data/base_cancel_reason_configurator_data.xml",
        "data/ir_sequence_data.xml",
        "data/base_sequence_configurator_data.xml",
        "data/base_workflow_policy_data.xml",
        "data/ir_filter_data.xml",
        "data/ir_actions_server_data.xml",
        "data/base_action_rule_data.xml",
        "data/ir_cron_data.xml",
        "menu.xml",
        "wizard/realize_interest_views.xml",
        "wizard/select_realization_entry_out_views.xml",
        "wizard/select_realization_entry_in_views.xml",
        "views/loan_type_views.xml",
        "views/loan_common_views.xml",
        "views/loan_payment_schedule_common_views.xml",
        "views/loan_in_views.xml",
        "views/loan_out_views.xml",
        "views/loan_in_payment_schedule_views.xml",
        "views/loan_out_payment_schedule_views.xml",
        "views/loan_config_setting_views.xml",
    ],
}
