import unittest
import bot_id
import wray.slacklib
import chris.slacklib

class TestSlackBotFunctions(unittest.TestCase):

    def test_ci(self):
        self.assertTrue(True)

    def test_slack_client(self):
        self.assertTrue(bot_id.get_id() == None)

    def test_wray_handler(self):
        self.assertFalse(wray.slacklib.handle_command('') == None)
        self.assertTrue(len(wray.slacklib.handle_command(
            wray.slacklib.COMMAND1)) > 1)
        resp = wray.slacklib.handle_command(wray.slacklib.COMMAND4)
        print(resp)
        self.assertTrue(len(resp) > 1)

    def test_chris_handler(self):
        self.assertFalse(chris.slacklib.handle_command('') == None)
        self.assertTrue(len(chris.slacklib.handle_command(
            chris.slacklib.COMMAND1)) > 1)


if __name__ == '__main__':
    unittest.main()
