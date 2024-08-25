import ete3

class PruneInternalsPlugin:
    def input(self, infile):
        treefile = open(infile, 'r')
        self.mytree = ete3.Tree(treefile.read(), format=1)

    def run(self):
        self.finalstring = ""
        i=0
        mytreestr = self.mytree.write(format=1)
        while (i < len(mytreestr)):
            if (i < len(mytreestr)-3):
                if (mytreestr[i:i+3] == 'INT'):
                    while (mytreestr[i] != ':'):
                        i += 1
            self.finalstring += mytreestr[i]
            i += 1

    def output(self, outputfile):
        outfile = open(outputfile, 'w')
        outfile.write(self.finalstring)
