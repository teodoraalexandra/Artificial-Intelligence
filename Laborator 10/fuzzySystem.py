#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 17 17:08:24 2020

@author: teodoradan
"""


class FuzzySystem:

    def __init__(self, rules):
        self.in_descriptions = {}
        self.out_description = None
        self.rules = rules

    def add_description(self, name, descr, out=False):
        if out:
            if self.out_description is None:
                self.out_description = descr
            else:
                raise ValueError('System already has an output')
        else:
            self.in_descriptions[name] = descr

    def compute(self, inputs):
        fuzzy_vals = self._compute_descriptions(inputs)
        rule_vals = self._compute_rules_fuzzy(fuzzy_vals)

        fuzzy_out_vars = [(list(descr[0].values())[0], descr[1]) for descr in
                          rule_vals]
        weighted_total = 0
        weight_sum = 0
        for var in fuzzy_out_vars:
            weight_sum += var[1]
            weighted_total += self.out_description.defuzzify(*var) * var[1]

        return weighted_total / weight_sum

    def _compute_descriptions(self, inputs):
        return {
            var_name: self.in_descriptions[var_name].fuzzify(inputs[var_name])
            for var_name, val in inputs.items()
        }

    def _compute_rules_fuzzy(self, fuzzy_vals): 
        return [rule.evaluate(fuzzy_vals) for rule in self.rules
                if rule.evaluate(fuzzy_vals)[1] != 0]