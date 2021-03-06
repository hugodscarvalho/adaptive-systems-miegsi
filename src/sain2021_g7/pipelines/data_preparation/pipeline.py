# Copyright 2021 QuantumBlack Visual Analytics Limited
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND
# NONINFRINGEMENT. IN NO EVENT WILL THE LICENSOR OR OTHER CONTRIBUTORS
# BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#
# The QuantumBlack Visual Analytics Limited ("QuantumBlack") name and logo
# (either separately or in combination, "QuantumBlack Trademarks") are
# trademarks of QuantumBlack. The License does not grant you any right or
# license to the QuantumBlack Trademarks. You may not use the QuantumBlack
# Trademarks or any confusingly similar mark as a trademark for your product,
# or use the QuantumBlack Trademarks in any other manner that might cause
# confusion in the marketplace, including but not limited to in advertising,
# on websites, or on software.
#
# See the License for the specific language governing permissions and
# limitations under the License.

"""
This is a boilerplate pipeline 'data_preparation'
generated using Kedro 0.17.2
"""

from kedro.pipeline import Pipeline, node
from .nodes import (
    linear_interpolation,
    add_date_range,
    standardize,
    ctgan_synthetic_generator,
    gaussian_copula_synthetic_generator,
)


def create_pipeline(**kwargs):

    return Pipeline(
        [
            node(
                func=linear_interpolation,
                inputs="prod_sales",
                outputs="prod_sales_filled",
                tags="fill",
            ),
            node(
                func=add_date_range,
                inputs=["prod_sales_filled", "parameters"],
                outputs="prod_sales_date_range",
                tags="date",
            ),
            # node(
            #     func=standardize,
            #     inputs="prod_sales_date_range",
            #     outputs=["prod_sales_standardized", "prod_sales_SCALER"],
            #     tags="standardize",
            #     ),
            # node(
            #     func=ctgan_synthetic_generator,
            #     inputs=["prod_sales_filled", "parameters"],
            #     outputs=["ctgan_synthetic_data", "CTGAN_eval"],
            #     tags="synthetic",
            #     ),
            # node(
            #     func=gaussian_copula_synthetic_generator,
            #     inputs=["prod_sales_filled", "parameters"],
            #     outputs=["gaussian_copula_synthetic_data", "GC_eval"],
            #     tags="synthetic",
            #     ),
            # node(
            #     func=add_date_range,
            #     name="CTGAN_Date_Range",
            #     inputs=["ctgan_synthetic_data", "parameters"],
            #     outputs="ctgan_synthetic_date_range",
            #     tags="date",
            #     ),
            # node(
            #     func=add_date_range,
            #     name="GaussianCopula_Date_Range",
            #     inputs=["gaussian_copula_synthetic_data", "parameters"],
            #     outputs="gaussian_copula_synthetic_date_range",
            #     tags="date",
            #     ),
        ]
    )
