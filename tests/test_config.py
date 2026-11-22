import unittest

from config import get_settings


class GetSettingsTests(unittest.TestCase):
    def test_defaults_are_used_when_values_are_missing_or_blank(self) -> None:
        settings = get_settings(
            {
                "AWS_REGION": "",
                "PROJECT_NAME": " ",
                "RETURNS_KB_ID": "",
                "SHIPPING_KB_ID": "  ",
            }
        )

        self.assertEqual(settings.aws_region, "us-east-1")
        self.assertEqual(settings.project_name, "udacity-agentcore")
        self.assertIsNone(settings.returns_kb_id)
        self.assertIsNone(settings.shipping_kb_id)
        self.assertIsNone(settings.warranty_kb_id)

    def test_configured_values_are_trimmed_and_loaded(self) -> None:
        settings = get_settings(
            {
                "AWS_REGION": " eu-west-1 ",
                "PROJECT_NAME": " shop-support ",
                "RETURNS_KB_ID": " returns-id ",
                "SHIPPING_KB_ID": "shipping-id",
                "WARRANTY_KB_ID": "warranty-id",
            }
        )

        self.assertEqual(settings.aws_region, "eu-west-1")
        self.assertEqual(settings.project_name, "shop-support")
        self.assertEqual(settings.returns_kb_id, "returns-id")
        self.assertEqual(settings.shipping_kb_id, "shipping-id")
        self.assertEqual(settings.warranty_kb_id, "warranty-id")


if __name__ == "__main__":
    unittest.main()
