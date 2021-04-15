all: atom_classes

.PHONY: atom_classes
atom_classes:
	cd grid && make atom_classes.py
	cd notes && make atom_classes.py
