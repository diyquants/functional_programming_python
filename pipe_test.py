from pipeline import Pipe

# パイプラインを開始するためのヘルパー (Pipeの省略形)
P = Pipe

resA = (P(range(10))
               | (lambda x:[y^2 for y in x])
               | (lambda x:[y+1 for y in x])
               | (lambda x:sum(x))
			   | print)
