### Being used right now

1. sex
2. age
3. prior arrests
4. jail time
5. charge degree
6. two year recidivism.

- These are set against the COMPAS scores.

### Questions

- What does the clustering reveal?
- How does it compare with the COMPAS scores?
- How does it compare with race?

### Not being used

- Juvenile felonies count
- Juvenile misdemeanors count
- Juvenile others count
- Prior charges count
- Days before screening arrest

### Other things we have

- The date when the test is being administered (is this meaningful?).

### Further ideas

- Comparing charge degree of "C" (first arrest) with charge degree of "R" and "V" (second arrest).
- Distance between score for general recidivism and violent recidivism. What crimes are more associated with one or the other?

### Perfecting the current plotting of distance

- Variables being used:
	- `sex`;
	- `age`;
	- prior arrests (`priors_count`);
	- charge degree (`c_charge_degree`);
	- jail time (`c_jail_in`, `c_jail_out`);
	- juvenile felonies (`juv_fel_count`);
	- juvenile misdemeanors (`juv_misd_count`);
	- juvenile others (`juv_other_count`);
	- type of charge?

- Visualize against:
	- compas score (`decile_score`);
	- `race`;
	- actual recidivism (`two_year_recid`; or _either_ `is_recid` or `is_violent_recid`).
