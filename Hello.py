# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Hello",
        page_icon="👋",
    )

    st.write("# Marketplace demo 👋")

    st.sidebar.success("Select a demo above.")

    col1, col2, col3 = st.columns(3)

    with col1:
      st.header("A cat")
      st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
      st.header("A dog")
      st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
      st.header("An owl")
      st.image("https://static.streamlit.io/examples/owl.jpg")


if __name__ == "__main__":
    run()
