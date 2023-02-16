#Purpose of this program is to create a fun, interactive game for high school chemistry students to test their general chemistry vocabulary

#credit for hangman and wordbank template: <script src="https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c"
#Hangman game code based on: https://www.youtube.com/watch?v=cJJTnI22IF8

#Here, I want to create a storage space for the images of hangman and chemistry terms
chemHangmanIcons = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of General Chemistry terms
genChemWords = ("acid, Arrhenius, base, Bronsted, chemistry, dissociation, density, electron, element"
          "Freezing, functional group, Gibbs free energy, Gamma emission, Half-reaction, Halogens, indicator, Ionic bond" 
          "Kinetic energy, kinetic theory, Le Châtelier's principle, Lattice energy, molarity, molality, nitrogen, Neutron"
          "osmotic pressure, Oxidation, peroxide, Periodic table, Radioactive decay, Raoult's law"
          "Supersaturated, Salt bridge, Thermodynamics, temperature, Uncertainty principle, Unimolecular reaction"
          "VSPER theory, valence electron, Wavelength").split()
 