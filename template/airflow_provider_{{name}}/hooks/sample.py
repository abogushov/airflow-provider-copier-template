from __future__ import annotations

from typing import Any, Tuple

from airflow.hooks.base import BaseHook


class SampleHook(BaseHook):
    """
    Sample Hook that print connection config.

    :param sample_conn_id: connection that has the base API url i.e https://www.google.com/
        and optional authentication credentials. Default headers can also be specified in
        the Extra field in json format.
    :type sample_conn_id: str
    """

    conn_name_attr = "sample_conn_id"
    default_conn_name = "sample_default"
    conn_type = "sample"
    hook_name = "Sample"

    def __init__(
        self,
        sample_conn_id: str = default_conn_name,
    ) -> None:
        super().__init__()
        self.sample_conn_id = sample_conn_id

    def run(
        self,
        **request_kwargs,
    ) -> Any:
        """
        Performs the request

        """
        if self.sample_conn_id:
            conn = self.get_connection(self.sample_conn_id)

        self.log.info(f"Use connection {{conn}}")

    def test_connection(self) -> Tuple[bool, str]:
        """Test a connection"""
        try:
            self.run()
            return True, "Connection successfully tested"
        except Exception as e:
            return False, str(e)
