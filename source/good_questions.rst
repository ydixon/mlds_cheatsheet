.. _good_questions:

================
Good Questions
================

.. contents:: :local:


.. rubric:: In what situations do neural networks outperform gradient boosting and random forest models on regular numeric and categorical data non image or text data if any?


There are some essential characteristics about deep learning neural nets that set them apart from algorithms like random forest and it has nothing to do with images or text per se. Random forest is very limited in a sense in what it can model well. This is very easy to see when applied to image data so let’s start there and then show why it has nothing intrinsically to do with images.

Lets say the images are all 256x256 images of cats and dogs and we want to classify them appropriately. A random forest is just an aggregation of decisions trees so let’s show why decisions trees are useless for problems like this.

If you treat the pixel bases as base feature (just as you do with NNs), random forest tries to choose a set of pixels randomly and then starts making a decision tree by cutting on the value of these pixels. First it looks for the pixel that best splits cats and dogs. We know that there is no such pixel. For a finite dataset, there will be one for sure that correlates slightly more than the others and so it will choose this one. But we know that is simply noise not real information. So it hasn’t really learned anything on the first choice. Now it needs to select a second pixel given each of the previous splits. Again, we know that there is really no good choice as two pixels don’t really differentiate cats and dogs.

What is going wrong? A decision tree is a greedy algorithm that can only make progress when each base features carries some reasonable amount of information. If they do, it can progress one feature at a time. But with images, this is not the case. It’s easy to see why. We know that whether an image is a cat or dog has nothing to do with any particular pixel. If you shift the images in some direction, it doesn’t change it cat/dog-ness. This approximate shift invariance is built into convolutional networks from the start. It’s basically starting with the assumption that it’s only correlation with local pixels that matter not the values of any particular pixel.

There is another thing that neural networks are doing. They are not greedy in the same sense. They aren’t making one choice about one parameter independent of all the others. When they make a gradient step, they are updating parameters that effect all parts of the image at all scales. A decision tree just looks at one pixel. By only looking at one pixel at a time, it can never really improve from where it was and never really progresses discover a good separation boundary. The real separation boundary in this high dimensional space is rarely perpendicular with the original basis (pixels).

Deep neural nets are intrinsically hierarchical in how they model things. It turns out that this is a natural fit for vision. We know that before we recognize a cat or dog, we need to know where the edges are so we can separate the animal from the background. Edges segments are one of the small high frequency features that a NN learns almost always. The hierarchical structure of the NN then allows these edges to be reused and combined to define many parts of the image like ears and noses, whiskers and claws. These features in turn can be combined into larger features like faces and body parts.

So we have learned three properties of NNs that differentiate it from random forests

    Can be given hints early on concerning what kinds of transformations it should be invariant to which allows it to avoid choosing poor initial features
    Doesn’t assume the base features to be informative individually or that it can progress by greedily optimizing along each base feature direction at a time.
    Naturally builds features hierarchically

The first feature is not really essential to NNs but is central to convolutional neural networks. It could be utilized with any other method. It’s possible that we might discover another technique for which specifying the invariants is the principle way in which we describe the model but that’s another topic.

Number 2 and 3 are huge advantage for computer vision. We know the information about what we are looking at is only revealed through how everything relates to everything else. Pixels are the extreme worst possible basis for that so random forest or any tree based method is being set up to fail here. Hierarchical feature generation is hugely beneficial for vision because we know that lines and edges and shapes are import base features for describing visual objects.

So we have enough information to guess where NNs would be more effective then random forest or tree based methods. It should be the case that the initial base features are individually un-informative. That’s not true for example with say credit worthiness. If all I know is your credit score, I can already make a decent prediction on your default rate. Having 100 other features helps for sure but even this one feature by itself moves me forward.

Let’s say I am trying to augment the (already decent) credit model based on the content of your tweets with word and word location (for example (baseball, position 7)) as our base features. Intuitively we might guess that no particular word/location is going to improve our model well. In fact, no small set of words will do that either.

What would matter? What if someone tweeted, “I just lost my job”. Could a random forest algorithm detect that this is important for credit worthiness? Yes. But it’s very unlikely. Why? Let’s say that a decision trees has made it to

“I just ___ my job”.

That is, it is looking at the fifth feature after correctly picking the first four word ordering pairs.

If it got here, it would probably do a good job at picking the next one. The word could be “love” or “lost” and the choice between them probably provides a lot of information. So if a decision trees got to this place, it would make progress. BUT, it would never make it here to begin with. Why would we expect it to make a first cut say on “___ ___ ___ my ___ ”. Would the presence of the word “my” in the 4th location by itself be informative on credit? No way.

A NN might make progress on this problem because it tries to work with word combinations and we know the real information of text data lives in the combinations and ordering of words and not simply words by themselves.

Furthermore, it can make progress because it can reuse hierarchical features. Words combine into phrases. Phrases combine into sentences. Sentences combines into higher level ideas. The important information can exist at any of those levels. NNs are still terrible at natural language processing to be sure and in my estimation will fail in this area. But they still beat the pants off things like random forest which really have no chance to learn meaning by looking at one word at a time.

Can we think of example of where the essential characteristics of NNs will matter that has nothing to do with vision or text? Try to think of anything where the base data is provided in a form for which a single data element carries essentially no information and all the information really comes from it is relation to other elements. It should be a case where low level features can be reused in a hierarchical fashion to form larger features or concepts.

Here are some things that come to mind for me

    A program for deciding which shot to take at pool
    Programs for directing soldiers in a batttle
    A program for forecasting the effect of cancer drugs given the genome and case history of the patient

Let’s take the second one. The information of one soldier on the field doesn’t change the mind of generals of what strategy to take. They think in terms of higher level concepts: platoons and divisions, fronts and flanks, morale and medical conditions. But these things are made up of smaller units like soldiers, roads and tanks. They want to decide on high level strategy based on these higher level concepts but needs to understand the properties of the low level objects in order to do so. They can’t expect a division to move 100 miles in a day if the tanks at top speed could only do 30 or if most of the soldiers are infantry. Everything is bound up by everything else. You can’t just move one soldier and then decide where to move the next soldier and so on. Perhaps the winning strategy is a massive attack on one weak part of the enemy line. But it is only a good strategy if it is large enough to break through. You don’t discover that strategy by moving one piece at a time greedily because each step in that direction is a failure until sufficiently large numbers are reached. You need to be thinking at a much higher level of abstraction but those higher level abstraction need to be built realistically and hierarchically from smaller reusable units.



https://www.quora.com/In-what-situations-do-neural-networks-outperform-gradient-boosting-and-random-forest-models-on-regular-numeric-and-categorical-data-non-image-or-text-data-if-any