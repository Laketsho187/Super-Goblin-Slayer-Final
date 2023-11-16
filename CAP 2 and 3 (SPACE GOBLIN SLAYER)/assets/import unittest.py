import unittest
from Space import Player # replace 'your_module' with the name of the module where Player is defined

class TestPlayer(unittest.TestCase):
   def setUp(self):
       self.player = Player(300, 60)

   def test_player_initialization(self):
       self.assertEqual(self.player.x, 300)
       self.assertEqual(self.player.y, 60)
       self.assertEqual(self.player.health, 100)
       self.assertEqual(self.player.ship_img, Player_Rocket)
       self.assertEqual(self.player.laser_img, Yellow_Laser)

if __name__ == '__main__':
   unittest.main()
