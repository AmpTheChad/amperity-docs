.. 
.. https://docs.amperity.com/reference/
.. 


.. meta::
    :description lang=en:
        Email addresses

.. meta::
    :content class=swiftype name=body data-type=text:
        Email addresses

.. meta::
    :content class=swiftype name=title data-type=string:
        Email addresses

==================================================
Email addresses
==================================================

.. include:: ../../shared/terms.rst
   :start-after: .. term-email-start
   :end-before: .. term-email-end


.. _attribute-customer-profile-email-segment:

Use in segments
==================================================

.. attribute-customer-profile-email-start

You can access email addresses directly from the **Segment Editor**. To add this attribute to your segment, click **Add condition** and then **Add attribute**. Select the **Customer 360** table, select the **Email** attribute, and then apply an condition.

.. attribute-customer-profile-email-end


.. _attribute-customer-profile-email-conditions:

Available conditions
==================================================

.. attribute-customer-profile-email-conditions-start

The following table lists the conditions that are available to this attribute.

.. note:: This attribute has a String data type. All String data types share the same set of conditions. Recommended conditions for this attribute are identified with "|attribute-recommended| **More useful**" and conditions with more limited use cases are identified with "|attribute-stop| **Less useful**".

.. list-table::
   :widths: 35 65
   :header-rows: 1

   * - Condition
     - Description

   * - **contains**
     - Returns customer records with values that match a string of characters.

   * - **does not contain**
     - Returns customer records with values that do not match a string of characters.

   * - **ends with**
     - Returns customer records with values that end with the specified characters.

   * - **is empty**
     - Returns customer records that do not have a value in this field.

   * - **is exactly**
     - Returns all customer records with values that match the specified characters.

   * - **is not empty**
     - Returns customer records that have a value in this field.

   * - **is not exactly**
     - Returns customer records that do not match the specified characters.

   * - **starts with**
     - Returns customer records that start with the specified characters.

.. attribute-customer-profile-email-conditions-end
