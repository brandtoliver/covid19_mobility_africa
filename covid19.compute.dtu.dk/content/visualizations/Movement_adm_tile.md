# **Movements between city tiles**
{{< fontsize 14 >}}*Data analysis by [Sebastian Andreasen](mailto:sstan@dtu.dk) and [Oliver Brandt](mailto:ob95@me.com).*{{< /fontsize >}}

{{< figures/globals >}}

The movement data can provide us with insights on how people are moving between different locations. In this case due to limited data, it has been decided to focus only on the larger cities in Kenya and Nigeria. The movements between tiles are shown for each time-slot. 

The map shows the outline of the selected city, while the edges represent movements between tiles within the city. The larger the size of the edges and particles is, the more people move between the tiles. 

* The **{{< color color="#c0392b" >}}red{{< /color >}}** edges means that there is less movement than the baseline.

* The **{{< color color="#1E90FF" >}}blue{{< /color >}}** edges means that there is more movement than the baseline.

{{< figures/movements_adm_tile >}}


<!-- {{< vspace 20 >}} -->

<!--
test

Using the Movement Maps we can visualize the distribution where people spend their days relative to their nights. While not accurate in every single case, it's perhaps easier to say that we are able to see where people *live* (spend their nights) and *work* (spend their nights). Or even more compactly, that we can look at commuting patterns over time.

Based on three daily time windows, the *Movement Maps* provide a "travel count" for some area *i* which is the number of active Facebook uses who spent the majority of the previous time window inside some other area *j*. As discussed in '**Data** > Movement Maps', this choice of aggregation by Facebook **implies that we cannot accurately assess the full amount of travel happening between and within regions**.

As noted above, however, we can reliably quantify which share of the population **spends the working hours away from home**. Specifically, given the way travel is aggregated in the Movement Maps, travel counts into regions/tiles in the night hours (16–00 window) represents the number of people that spend the majority of their working hours (8—16) somewhere else. Thus, it's not unreasonable to think of these travel counts as representing people **commuting**.

**The map below** looks at day-to-day between-municipality commuting patterns before and after the lockdown. By default the map displays *Change*, which is the percentage deviation between the size of the working population on the date selected with the slider, and the corresponding baseline (before lockdown). Clicking *On date* shows value for the date selected in the slider and *Baseline* for the corresponding baseline day. You can click any municipality to reveal where people who live there go to work.

A general pattern is that people who live in urban municipalities also work where they live, whereas people who live in municipalities next to more urbanized municipalities tend to work away from their home municipality.

When moving the slider through time it is clear that that the deviation—the *change*—between *Baseline* and *On date* decreases. This is the same pattern that we summarize in '**Visualizations** > Staying home' and '**Visualizations** > Going out'.

{{< figures/movements_adm_tile >}}

> **This figure is interactive!** You can:
> * **Hover** the curser over an administrative region to display the share of the Facebook population that makes daily journeys we assume represents work.
> * **Click** any administrative region to see where the population in that region goes to work.
> * **Drag** the time slider to display data for different dates.
> * **Select** either to display valus for the selected date (*On date*), the *Baseline* or the percentage deviation between these (*Change*).
> * **Hold** `shift` key after having selected (clicked) a region to display where people who work there live (as opposed to the default: where people who live there work).
> * **Press** the escape key to unselect a region.

*Note*: When clicking an administrative region, *Change* values displayed on other regions can be dramatically large. This is because, typically, only a small share of region populations work outside their home region, and because of the deviation calculation is as simple as (*A* - *B*) / *B*, they can blow up if *B* is small.
--> 