import os

inputfile = os.path.abspath(os.path.join('.', '{}'.format(input('Enter filename to open: '))))
infile = os.path.abspath(os.path.join('.', 'reachable.txt'))
outfile = os.path.abspath(os.path.join('.', 'unreachable.txt'))

count_reachable_hosts = 0
count_unreachable_hosts = 0
count_total_hosts = 0
list_of_unreachable = list()
list_of_reachable = list()

with open(inputfile) as hosts:
    for host in hosts:
        count_total_hosts += 1
        host.strip()
        if os.system('ping -c 1 -w 1 {}'.format(host)) == 0:
            print('{} is reachable'.format(host))
            count_reachable_hosts += 1
            list_of_reachable.append(host)
        else:
            print('{} is unreachable.'.format(host))
            count_unreachable_hosts += 1
            list_of_unreachable.append(host)



print()
print('---------------------------')
print('Results:')
print(f'{count_reachable_hosts} of {count_total_hosts} reachable')
print('{0} of {1} unreachable'.format(count_unreachable_hosts, count_total_hosts))
print('---------------------------')


print('writing to file...\n')

with open(infile, 'w') as fout:
    for reachable in list_of_reachable:
        fout.write(reachable)

with open(outfile, 'w') as fout:
    for unreachable in list_of_unreachable:
        fout.write(unreachable)
