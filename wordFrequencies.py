from mrjob.job import MRJob

class MRWordFrequency(MRJob):
    def mapper(self, k, line):
        for w in line.split():
            yield w, l

    def reducer(selfself, key, values):
        s = sum(values)
        yield key, s

    def combiner(self, key, values):
        s = sum(values)
        yield key, s

if __name__ == '__main__':
    MRWordFrequency.run()

# Running commands
# $python word_freq.py -r dataproc data.txt <-this is google cloud, latency very large, use only if job is big

# $python word_freq.py data.txt
# $python word_freq.py -r emr data.txt