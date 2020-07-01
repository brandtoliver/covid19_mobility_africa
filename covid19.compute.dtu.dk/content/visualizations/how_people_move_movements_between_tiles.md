# **Movements between city tiles**
{{< fontsize 14 >}}*Data analysis by [Sebastian Andreasen](mailto:s153522@dtu.dk) and [Oliver Brandt](mailto:ob95@me.com).*{{< /fontsize >}}

{{< figures/globals >}}

**Pick a city - either Nairobi or Mombasa in Kenya or Lagos or Abuja in Nigeria to the right &#8594;**
<!-- {{< vspace 20 >}} -->

Similar to the visualisation of ´Movement between municipalities´ we can visualize the distribution where people spend their days relative to their nights. This visualisation is made to explore the movement patterns over time within a city. 

This visualisation also based on the three daily time windows and movement of people are calculated exactly the same like the Movement Maps except that is it done between tiles instead of municipalities. For a detailed explanation of the movements are calculated see REF REF REF.

**The map below** displays the day-to-day between-tile travel patterns in a city. By default the map displays *Change*, which is the percentage deviation between the size of the working population on the date selected with the slider, and the corresponding baseline (before lockdown). Clicking *On date* shows value for the date selected in the slider and *Baseline* for the corresponding baseline day. You can click any tile to reveal where people who live there go to work.

In this map, only movement within the same city in regarded, meaning movement in and out of the city is not included. A general trend of the two Nigerian cities, is that we see that the deviation (*change* between *Baseline* and *On date*) decrease over time, similar to what is observed in the ´Movement between municipalities´. This percent change is 'very' negative from the start of the period until around end of April, where the travel patterns within in the city seems to start returning to the baseline.

{{< figures/movements_between_tiles >}}

> **This figure is interactive!** You can:
> * **Hover** the curser over an tile to display the share of the Facebook population that makes daily journeys we assume represents work.
> * **Click** any tile to see where the population in that tile goes to work.
> * **Drag** the time slider to display data for different dates.
> * **Select** either to display valus for the selected date (*On date*), the *Baseline* or the percentage deviation between these (*Change*).
> * **Hold** `shift` key after having selected (clicked) a tile to display where people who work there live (as opposed to the default: where people who live there work).
> * **Press** the escape key to unselect a tile.
