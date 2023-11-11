import frhd
import pyperclip

my_track = frhd.Track.Track()
my_track.addText(50,-50,"Hello. this is a test of my new auto text rendering system. Info in desc. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi consequat sed enim ut consectetur. Aliquam dictum convallis feugiat. Nunc iaculis eu libero cursus bibendum. Aliquam egestas risus sem, vehicula rutrum lorem laoreet ut. Suspendisse faucibus rutrum felis quis mattis. Suspendisse purus lorem, venenatis a arcu at, lobortis convallis lectus. Nam cursus mauris sit amet risus rhoncus aliquam. Etiam maximus quam nec enim rhoncus, in dictum erat pulvinar. Mauris felis nisi, porttitor id ligula sed, luctus congue urna.")
my_track.insLine("p", 0,50,10000,-50)

code = my_track.genCode()
pyperclip.copy(code)
print("copied to clipboard")
print(code)