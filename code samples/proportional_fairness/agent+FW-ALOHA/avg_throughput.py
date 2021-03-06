import numpy as np
import matplotlib.pyplot as plt


def my_plot(file1, file2, W):
	max_iter = 500000
	N = 10000

	# load reward
	agent1_reward = np.loadtxt(file1)
	agent2_reward = np.loadtxt(file2)

	throughput_agent1 = np.zeros((1, max_iter))
	throughput_agent2 = np.zeros((1, max_iter))


	# if q < 0.5:
	# 	agent1_optimal = np.ones(max_iter)* (1-q)
	# 	agent2_optimal = np.ones(max_iter)* 0
	# elif q > 0.5:	
	# 	agent1_optimal = np.ones(max_iter)* 0
	# 	agent2_optimal = np.ones(max_iter)* q




	agent1_temp_sum = 0
	agent2_temp_sum = 0
	# agent4_temp_sum = 0
	for i in range(0, max_iter):
		if i < N:
			agent1_temp_sum += agent1_reward[i]
			agent2_temp_sum += agent2_reward[i]
			# agent4_temp_sum += agent4_reward[i]
			throughput_agent1[0][i] = agent1_temp_sum / (i+1)
			throughput_agent2[0][i] = agent2_temp_sum / (i+1)
		else:
			agent1_temp_sum += agent1_reward[i] - agent1_reward[i-N]
			agent2_temp_sum += agent2_reward[i] - agent2_reward[i-N]
			throughput_agent1[0][i] = agent1_temp_sum / N
			throughput_agent2[0][i] = agent2_temp_sum / N

	plt.xlim((0, max_iter))
	plt.ylim((-0.05, 1))
	throughput_total = throughput_agent1[0]+throughput_agent2[0]
	agent1_line, = plt.plot(throughput_agent1[0], color='r', lw=1.2, label='agent')
	agent2_line, = plt.plot(throughput_agent2[0], color='b', lw=1.2, label='aloha')
	agent3_line, = plt.plot(throughput_total, color='k', lw=1.2, label='total')

	print(np.max(throughput_total[-10000:]))
	# agent3_line, = plt.plot(agent1_optimal, color='r', lw=3, label='agent optimal')
	# agent4_line, = plt.plot(agent2_optimal, color='b', lw=3, label='aloha optimal')
	plt.grid()
	# plt.legend(handles=[agent1_line, agent2_line, agent3_line, agent4_line], loc='best')
	print('---------------')
	print('agent', np.mean(throughput_agent1[0][-1]))
	print('aloha', np.mean(throughput_agent2[0][-1]))


for i in range(4, 5):
	plt.figure(i)
	my_plot('rewards/agent_len5e5_M20_h6_W2_%d.txt' % i,
		    'rewards/aloha_len5e5_M20_h6_W2_%d.txt' % i, W=5)
plt.show()

