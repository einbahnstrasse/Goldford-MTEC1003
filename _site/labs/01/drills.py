import random, os
commands = []
commands.append({
	'"a command"': 'a verb that tells the computer to do something',
	'"an argument"': 'the thing ("noun") that a command acts on',
	'"a flag"': 'specifies how a command should be run ("adverb")',
	'<TAB>': 'auto complete command and directory / files',
	'<TAB><TAB>': 'auto complete *all* potential commands and directory / files',
	'<UP>': 'show previous command',
	'<DOWN>': 'show next command'
})

commands.append({
	'pathname':'definition is: "specifies the location of a file"',
	'/ (forward slash)':'the character that\'s the path separator on OSX',
	'/Users/student/Desktop':'the absolute path to the student user\'s Desktop',
	'/Users/students':'absolute path to the student user\'s home directory',
	'/Volumes':'the directory where all disks attached to your computer is stored',
	'pwd':'print working directory',
	'hostname':'display name of computer',
	'mkdir':'make a directory', 
	'cd':'change directory',
	'  . (dot)': 'current directory',
	'  ..  (dot dot)': 'up one directory',
	'  ../..  (dot dot slash dot dot) ': 'up two directories',
	'  /  (slash)': 'root directory',
	'  ~  (tilde)':'home directory',
	'  -  (dash)':'previous directory',
	'ls':'list contents of current directory',
	'rmdir':'remove a directory',
	'pushd':'save current directory',
	'popd': 'go to most recent saved directory'
})

commands.append({
	'touch':'create new file',
	'copy':'copy file',
	'mv':'move file',
	'less':'show contents of file (starts with l)',
	'more':'show contents of file (starts with m)',
	'cat':'show contents of file (starts with c)',
	'rm':'remove file or directory'
})

commands.append({
	'find':'find files',
	'grep':'find files containing text',
})

s = raw_input('Enter flash card sets to use (1, 2, 3, 4):\n\n>')
set_indexes = [int(i) - 1 for i in list(s)]
d = commands[set_indexes[0]]
for n in set_indexes:
	d.update(commands[n])

cmd = ''
count = 1
count_loops = 1
while cmd.lower() != 'q':
	keys = list(d.keys())
	random.shuffle(keys)
	while keys:
		os.system('clear')
		print('%s: %s/%s' % (count_loops, count, len(d)))
		k = keys.pop()
		cmd = raw_input('\n    ' + d[k] + '\n    ')
		cmd = raw_input('    > ' + k)
		count += 1
	count = 1
	count_loops += 1
