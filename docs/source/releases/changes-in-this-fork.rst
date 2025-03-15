
Changes in this Fork
=====================

.. admonition :: A Word of Warning
    :class: tip
    
    We merge changes made to few of pyrogram forks plus changes made by us to this repository. All the features are just customized feature mostly for personal use; there is no guarantee in them being stable, **USE AT YOUR OWN RISK**.


This page lists all the documented changes of this fork,
in reverse chronological order. You should read this when upgrading
to this fork to know where your code can break, and where
it can take advantage of new goodies!

`For a more detailed description, please check the commits. <https://github.com/TelegramPlayGround/pyrogram/commits/dev/>`__

If you found any issue or have any suggestions, feel free to make `an issue <https://github.com/TelegramPlayGround/pyrogram/issues>`__ on github.

Breaking Changes in this Fork
==============================

- In :meth:`~pyrogram.Client.download_media`, if the message is a :obj:`~pyrogram.types.PaidMediaInfo` with more than one ``paid_media`` **and** ``idx`` was not specified, then a list of paths or binary file-like objects is returned.
- PR `#115 <https://github.com/TelegramPlayGround/pyrogram/pull/115>`_ This `change <https://github.com/pyrogram/pyrogram/pull/966#issuecomment-1108858881>`_ breaks some usages with offset-naive and offset-aware datetimes.
- PR from upstream: `#1411 <https://github.com/pyrogram/pyrogram/pull/1411>`_ without attribution.
- If you relied on internal types like ``import pyrogram.file_id`` OR ``import pyrogram.utils``, Then read this full document to know where `else <https://t.me/PyrogramChat/42497>`_ your code will break.


Changes in this Fork
=====================

+------------------------+
| Scheme layer used: 200 |
+------------------------+

- Rename ``UserGift`` to :obj:`~pyrogram.types.ReceivedGift`, ``get_user_gifts`` to :meth:`~pyrogram.Client.get_received_gifts` and the corresponding fields appropriately.
- Added the field ``paid_message_star_count`` to the classes :obj:`~pyrogram.types.Chat`, :obj:`~pyrogram.types.Message` and :obj:`~pyrogram.types.User`.
- Added the parameter ``paid_message_star_count`` to the methods :meth:`~pyrogram.Client.copy_media_group`, :meth:`~pyrogram.Client.send_game`, :meth:`~pyrogram.Client.send_invoice`, :meth:`~pyrogram.Client.forward_messages`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_audio`, :meth:`~pyrogram.Client.send_cached_media`, :meth:`~pyrogram.Client.send_contact`, :meth:`~pyrogram.Client.send_dice`, :meth:`~pyrogram.Client.send_document`, :meth:`~pyrogram.Client.send_location`, :meth:`~pyrogram.Client.send_media_group`, :meth:`~pyrogram.Client.send_message`, :meth:`~pyrogram.Client.send_paid_media`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_poll`, :meth:`~pyrogram.Client.send_sticker`, :meth:`~pyrogram.Client.send_venue`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_voice` and the bound methods :meth:`~pyrogram.types.Message.forward` and :meth:`~pyrogram.types.Message.copy`.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=199&to=200>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=199&to=200>`__.

+------------------------+
| Scheme layer used: 199 |
+------------------------+

- Added the class :obj:`~pyrogram.types.InlineQueryResultGame`.
- Added the bound methods :meth:`~pyrogram.types.ChosenInlineResult.edit_message_text`, :meth:`~pyrogram.types.ChosenInlineResult.edit_message_caption`, :meth:`~pyrogram.types.ChosenInlineResult.edit_message_media` and :meth:`~pyrogram.types.ChosenInlineResult.edit_message_reply_markup`.
- Renamed the fields ``thumb_url``, ``thumb_width``, and ``thumb_height`` in the classes :obj:`~pyrogram.types.InlineQueryResultArticle`, :obj:`~pyrogram.types.InlineQueryResultContact`, :obj:`~pyrogram.types.InlineQueryResultDocument`, :obj:`~pyrogram.types.InlineQueryResultLocation`, and :obj:`~pyrogram.types.InlineQueryResultVenue` to ``thumbnail_url``, ``thumbnail_width``, and ``thumbnail_height`` respectively.
- Renamed the field ``thumb_url`` in the classes :obj:`~pyrogram.types.InlineQueryResultPhoto` and :obj:`~pyrogram.types.InlineQueryResultVideo` to ``thumbnail_url``.
- Added the field ``animation_mime_type`` and renamed the fields ``thumb_url`` and ``thumb_mime_type`` in the classes :obj:`~pyrogram.types.InlineQueryResultAnimation` to ``thumbnail_url`` and ``thumbnail_mime_type`` respectively.
- Fixed a bug with ``_client`` being None in :obj:`~pyrogram.handlers.ChosenInlineResultHandler`.
- Added the parameters ``video_cover`` and ``video_start_timestamp`` to the method :meth:`~pyrogram.Client.copy_message`, allowing bots to change the start timestamp for copied videos.
- Added ``for_paid_reactions`` in :meth:`~pyrogram.Client.get_send_as_chats`.
- `Updated documentation and parameter names according to BOT API 8.3 <https://github.com/TelegramPlayGround/pyrogram/commit/7675b40>`__
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=198&to=199>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=198&to=199>`__.

+------------------------+
| Scheme layer used: 198 |
+------------------------+

- Updated :doc:`Text Formatting <../../topics/text-formatting>` documentation.
- Splitted the :meth:`~pyrogram.Client.get_messages` into :meth:`~pyrogram.Client.get_chat_pinned_message`, :meth:`~pyrogram.Client.get_callback_query_message`, and :meth:`~pyrogram.Client.get_replied_message`.
- Added ``message.content`` property.
- Added the ``cover`` and ``start_timestamp`` parameters in :meth:`~pyrogram.Client.send_video` and :obj:`~pyrogram.types.InputPaidMediaVideo`.
- Added the ``video_start_timestamp`` and renamed the ``send_copy`` and ``remove_caption`` parameters in :meth:`~pyrogram.Client.forward_messages` and :meth:`~pyrogram.types.Message.forward`.
- Added the ``gift_count`` to the :obj:`~pyrogram.types.Chat`.
- Added the :meth:`~pyrogram.Client.get_similar_bots`.
- Changed types in :obj:`~pyrogram.types.UpgradedGift`, :obj:`~pyrogram.types.UserGift`.
- PR from upstream: `701 <https://github.com/pyrogram/pyrogram/pull/701>`_
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=196&to=198>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=196&to=198>`__.

+------------------------+
| Scheme layer used: 196 |
+------------------------+

- Added the :meth:`~pyrogram.Client.get_owned_star_count` and a possibly temporary :obj:`~pyrogram.types.StarAmount`.
- Added the :obj:`~pyrogram.types.UpgradedGift` and changed return type :meth:`~pyrogram.Client.get_available_gifts` and :meth:`~pyrogram.Client.get_user_gifts`.
- Added the ``pay_for_upgrade`` in the :meth:`~pyrogram.Client.send_gift`.
- Added the parameters ``upgrade_star_count`` and ``is_for_birthday`` in :obj:`~pyrogram.types.Gift`.
- Added the :meth:`~pyrogram.Client.on_bot_purchased_paid_media` and :meth:`~pyrogram.Client.on_bot_business_connection`.
- Added the parameters ``can_be_upgraded``, ``was_refunded``, ``prepaid_upgrade_star_count``, ``can_be_transferred``, ``transfer_star_count``, ``export_date`` in :obj:`~pyrogram.types.UserGift`.
- Renamed the parameter ``only_in_channels`` to ``chat_type_filter`` in the :meth:`~pyrogram.Client.search_global_count` and :meth:`~pyrogram.Client.search_global`.
- Removed ``sender_user_id`` parameter from :meth:`~pyrogram.Client.sell_gift` and :meth:`~pyrogram.Client.toggle_gift_is_saved`.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=195&to=196>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=195&to=196>`__.

+------------------------+
| Scheme layer used: 195 |
+------------------------+

- Added the :meth:`~pyrogram.Client.get_owned_bots` to return the list of owned by the current user bots.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=194&to=195>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=194&to=195>`__.

+------------------------+
| Scheme layer used: 194 |
+------------------------+

- Added the field ``schedule_date`` and changed the return type of the :meth:`~pyrogram.Client.send_inline_bot_result`.
- Added the field ``subscription_expiration_date`` in the :obj:`~pyrogram.types.SuccessfulPayment`.
- Added the parameter ``subscription_period`` in the :meth:`~pyrogram.Client.create_invoice_link`.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=192&to=194>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=192&to=194>`__.

+------------------------+
| Scheme layer used: 192 |
+------------------------+

- Added :obj:`~pyrogram.enums.ChatEventAction.SHOW_MESSAGE_SENDER_ENABLED`, :obj:`~pyrogram.enums.ChatEventAction.AGGRESSIVE_ANTI_SPAM_TOGGLED`, :obj:`~pyrogram.enums.ChatEventAction.PROTECTED_CONTENT_TOGGLED`, :obj:`~pyrogram.enums.ChatEventAction.CHAT_IS_FORUM_TOGGLED`, :obj:`~pyrogram.enums.ChatEventAction.USERNAMES_CHANGED`, :obj:`~pyrogram.enums.ChatEventAction.MEMBER_SUBSCRIPTION_EXTENDED`, :obj:`~pyrogram.enums.ChatEventAction.MEMBER_JOINED_BY_LINK`, :obj:`~pyrogram.enums.ChatEventAction.MEMBER_JOINED_BY_REQUEST`, and updated :obj:`~pyrogram.types.ChatEventFilter` with the corresponding attributes.
- Added the parameter ``show_caption_above_media`` to the :meth:`~pyrogram.Client.edit_inline_caption`.
- Added the parameter ``allow_paid_broadcast`` to the methods :meth:`~pyrogram.Client.copy_media_group`, :meth:`~pyrogram.Client.send_game`, :meth:`~pyrogram.Client.send_invoice`, :meth:`~pyrogram.Client.forward_messages`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_audio`, :meth:`~pyrogram.Client.send_cached_media`, :meth:`~pyrogram.Client.send_contact`, :meth:`~pyrogram.Client.send_dice`, :meth:`~pyrogram.Client.send_document`, :meth:`~pyrogram.Client.send_location`, :meth:`~pyrogram.Client.send_media_group`, :meth:`~pyrogram.Client.send_message`, :meth:`~pyrogram.Client.send_paid_media`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_poll`, :meth:`~pyrogram.Client.send_sticker`, :meth:`~pyrogram.Client.send_venue`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_voice` and the bound methods :meth:`~pyrogram.types.Message.reply_game`, :meth:`~pyrogram.types.Message.reply_text`, :meth:`~pyrogram.types.Message.reply_animation`, :meth:`~pyrogram.types.Message.reply_audio`, :meth:`~pyrogram.types.Message.reply_contact`, :meth:`~pyrogram.types.Message.reply_document`, :meth:`~pyrogram.types.Message.reply_location`, :meth:`~pyrogram.types.Message.reply_media_group`, :meth:`~pyrogram.types.Message.reply_photo`, :meth:`~pyrogram.types.Message.reply_poll`, :meth:`~pyrogram.types.Message.reply_sticker`, :meth:`~pyrogram.types.Message.reply_venue`, :meth:`~pyrogram.types.Message.reply_video`, :meth:`~pyrogram.types.Message.reply_video_note`, :meth:`~pyrogram.types.Message.reply_voice`, :meth:`~pyrogram.types.Message.reply_invoice`, :meth:`~pyrogram.types.Message.forward`, :meth:`~pyrogram.types.Message.copy`, :meth:`~pyrogram.types.Message.reply_cached_media`.
- Introduced the ability to add media to existing text messages using the method :meth:`~pyrogram.Client.edit_message_media`, :meth:`~pyrogram.Client.edit_cached_media`, :meth:`~pyrogram.types.Message.edit_media`, :meth:`~pyrogram.types.Message.edit_cached_media`.
- Added the class :obj:`~pyrogram.types.CopyTextButton` and the field ``copy_text`` in the class :obj:`~pyrogram.types.InlineKeyboardButton` allowing bots to send and receive inline buttons that copy arbitrary text.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=190&to=192>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=190&to=192>`__.

+------------------------+
| Scheme layer used: 190 |
+------------------------+

- Added the methods :meth:`~pyrogram.Client.get_available_gifts`, :meth:`~pyrogram.Client.get_user_gifts`, :meth:`~pyrogram.Client.sell_gift`, :meth:`~pyrogram.Client.send_gift`, :meth:`~pyrogram.Client.toggle_gift_is_saved`, :meth:`~pyrogram.types.UserGift.toggle` and the types :obj:`~pyrogram.types.UserGift` and :obj:`~pyrogram.types.Gift`.
- Added the parameter ``send_as`` in the appropriate methods and bound methods `PR 107 <https://github.com/TelegramPlayGround/pyrogram/pull/107>`_.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=189&to=190>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=189&to=190>`__.

+------------------------+
| Scheme layer used: 189 |
+------------------------+

- Added :meth:`~pyrogram.Client.toggle_forum_topic_is_pinned` to pin / unpin a :obj:`~pyrogram.types.ForumTopic`.
- Added :meth:`~pyrogram.types.Message.star` bound method to the :obj:`~pyrogram.types.Message`.
- Added the field ``alternative_videos`` to the :obj:`~pyrogram.types.Message`.
- Added the fields ``connected_website`` and ``write_access_allowed`` to the :obj:`~pyrogram.types.Message`.
- Fix ``chat`` being None in some cases in the :obj:`~pyrogram.types.Message`.
- Fix deleting messages does not return the count in some cases.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=187&to=189>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=187&to=189>`__.

+------------------------+
| Scheme layer used: 187 |
+------------------------+

- Added the parameter ``emoji`` in :meth:`~pyrogram.Client.send_sticker` and :meth:`~pyrogram.types.Message.reply_sticker`. `#86 <https://github.com/KurimuzonAkuma/pyrogram/pull/86>`__.
- `Return list of photos and videos instead of bool in send_payment_form <https://github.com/KurimuzonAkuma/pyrogram/commit/6684eaf4273b0f2084a8709e2e852486f17cb67c>`__.
- Added the field ``prize_star_count`` to the classes :obj:`~pyrogram.types.GiveawayCreated`, :obj:`~pyrogram.types.Giveaway`, :obj:`~pyrogram.types.GiveawayWinners`.
- Added the field ``is_star_giveaway`` to the class :obj:`~pyrogram.types.GiveawayCompleted`.
- Added the ability to specify a payload in :meth:`~pyrogram.Client.send_paid_media` that is unused currently.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=186&to=187>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=186&to=187>`__.

+------------------------+
| Scheme layer used: 186 |
+------------------------+

- Try to return the service message (when applicable) in the methods :meth:`~pyrogram.Client.set_chat_photo`, :meth:`~pyrogram.types.Chat.set_photo`.
- Added the methods :meth:`~pyrogram.Client.get_payment_form` and :meth:`~pyrogram.Client.send_payment_form` `#89 <https://github.com/TelegramPlayGround/pyrogram/pull/89>`__.
- Added the fields ``expired_member_count``, ``subscription_period`` and ``subscription_price`` to the class :obj:`~pyrogram.types.ChatInviteLink`.
- Added the field ``can_enable_paid_reaction`` to the class :obj:`~pyrogram.types.Chat`.
- Added ``link`` property to :obj:`~pyrogram.types.Story` and fixed the ``link`` property in :obj:`~pyrogram.types.Message`.
- Introduced :obj:`~pyrogram.types.DraftMessage` type.
- Added the ability to send paid media to any chat and the parameter ``business_connection_id`` to the :meth:`~pyrogram.Client.send_paid_media`, allowing bots to send paid media on behalf of a business account.
- Added the field ``until_date`` to the class :obj:`~pyrogram.types.ChatMember` for members with an active subscription.
- Added :meth:`~pyrogram.Client.add_paid_message_reaction` and :obj:`~pyrogram.types.ReactionTypePaid`
- Updated `errors list <https://core.telegram.org/api/errors>`__ and improved documentation of some of the methods.
- Added missing parameters to :meth:`~pyrogram.Client.get_dialogs` and :obj:`~pyrogram.types.Dialog`.
- Added :obj:`~pyrogram.enums.MessageServiceType.UNKNOWN` type of service message `#1147 <https://github.com/pyrogram/pyrogram/issues/1147>`__.
- Added a :obj:`~pyrogram.enums.ChatJoinType` to distinguish the different types of :obj:`~pyrogram.enums.MessageServiceType.NEW_CHAT_MEMBERS`.
- Added :obj:`~pyrogram.enums.MessageServiceType.CONTACT_REGISTERED` and :obj:`~pyrogram.enums.MessageServiceType.SCREENSHOT_TAKEN` types of service messages.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=185&to=186>`__ raw API methods.


+------------------------+
| Scheme layer used: 185 |
+------------------------+

- Added the parameter ``chat_list`` to the methods :meth:`~pyrogram.Client.get_dialogs` and :meth:`~pyrogram.Client.get_dialogs_count`.
- Added ``gifted_stars`` service message to the class :obj:`~pyrogram.types.Message`.
- Added the fields ``have_access``, ``has_main_web_app``, ``active_user_count`` to the class :obj:`~pyrogram.types.User`, which is returned in response to  :meth:`~pyrogram.Client.get_me`.
- Added the parameter ``business_connection_id`` to the methods :meth:`~pyrogram.Client.pin_chat_message` and :meth:`~pyrogram.Client.unpin_chat_message`, allowing bots to manage pinned messages on behalf of a business account.
- View `new and changed <https://telegramplayground.github.io/TG-APIs/TL/diff/tdlib.html?from=184&to=185>`__ `raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=184&to=185>`__.


+------------------------+
| Scheme layer used: 184 |
+------------------------+

- Updated :obj:`~pyrogram.filters.via_bot`, to optionally support filtering invalid bot ``user_id``.
- Added the :meth:`~pyrogram.Client.get_active_sessions`, :meth:`~pyrogram.Client.terminate_session`, :meth:`~pyrogram.types.ActiveSession.terminate`, and :meth:`~pyrogram.Client.terminate_all_other_sessions`.
- Added the ``is_automatic_forward`` to the :obj:`~pyrogram.types.Message`.
- Added the parameters ``offset_id`` to the :meth:`~pyrogram.Client.search_messages` and the parameters ``min_date``, ``max_date``, ``min_id``, ``max_id``, ``saved_messages_topic_id`` to the :meth:`~pyrogram.Client.search_messages_count`.
- Dynamic session ReStart + restart optimizations (`#56 <https://github.com/TelegramPlayGround/pyrogram/pull/56>`__)
- Added the :meth:`~pyrogram.Client.delete_account`, :meth:`~pyrogram.Client.transfer_chat_ownership`, :meth:`~pyrogram.Client.update_status` (`#49 <https://github.com/TelegramPlayGround/pyrogram/pull/49>`__, `#51 <https://github.com/TelegramPlayGround/pyrogram/pull/51>`__)
- Added the class :obj:`~pyrogram.types.RefundedPayment`, containing information about a refunded payment.
- Added the field ``refunded_payment`` to the class :obj:`~pyrogram.types.Message`, describing a service message about a refunded payment.
- `View new and changed raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=183&to=184>`__.


+------------------------+
| Scheme layer used: 183 |
+------------------------+

- Added the classes :obj:`~pyrogram.types.PaidMedia`, :obj:`~pyrogram.types.PaidMediaInfo`, :obj:`~pyrogram.types.PaidMediaPreview`, :obj:`~pyrogram.types.PaidMediaPhoto` and :obj:`~pyrogram.types.PaidMediaVideo`, containing information about paid media.
- Added the method :meth:`~pyrogram.Client.send_paid_media` and the classes :obj:`~pyrogram.types.InputPaidMedia`, :obj:`~pyrogram.types.InputPaidMediaPhoto` and :obj:`~pyrogram.types.InputPaidMediaVideo`, to support sending paid media.
- Added the field ``paid_media`` to the classes :obj:`~pyrogram.types.Message` and :obj:`~pyrogram.types.ExternalReplyInfo`.
- Added :meth:`~pyrogram.Client.get_stories`.
- Added filters :obj:`~pyrogram.filters.thread` and :obj:`~pyrogram.filters.self_destruct`.
- Added the field ``can_send_paid_media`` to the class :obj:`~pyrogram.types.Chat`.
- Added support for launching Web Apps via ``t.me`` link in the class :obj:`~pyrogram.types.MenuButtonWebApp`.
- `View new and changed raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=181&to=183>`__.

+------------------------+
| Scheme layer used: 182 |
+------------------------+

- Updated the parameter ``business_connection_id`` to the methods :meth:`~pyrogram.types.Message.edit_text`, :meth:`~pyrogram.types.Message.edit_media`, :meth:`~pyrogram.types.Message.edit_reply_markup`, :meth:`~pyrogram.types.CallbackQuery.edit_message_text`, :meth:`~pyrogram.types.CallbackQuery.edit_message_media`, :meth:`~pyrogram.types.CallbackQuery.edit_message_reply_markup`.
- Added the parameter ``business_connection_id`` to the methods :meth:`~pyrogram.Client.edit_message_text`, :meth:`~pyrogram.Client.edit_message_media`, :meth:`~pyrogram.Client.edit_cached_media`, :meth:`~pyrogram.Client.edit_message_caption` and :meth:`~pyrogram.Client.edit_message_reply_markup`, allowing the bot to edit business messages.
- Added the parameter ``business_connection_id`` to the method :meth:`~pyrogram.Client.stop_poll`, allowing the bot to stop polls it sent on behalf of a business account.
- Added support for callback queries originating from a message sent on behalf of a business account.

+------------------------+
| Scheme layer used: 181 |
+------------------------+

- Added the classes :obj:`~pyrogram.types.InputLocationMessageContent`, :obj:`~pyrogram.types.InputVenueMessageContent`, :obj:`~pyrogram.types.InputContactMessageContent`, :obj:`~pyrogram.types.InputInvoiceMessageContent`.`
- Added ``background`` to :obj:`~pyrogram.types.Chat` (`#40 <https://github.com/TelegramPlayGround/pyrogram/pull/40>`_)
- Added the methods :meth:`~pyrogram.Client.translate_text`, :meth:`~pyrogram.Client.translate_message_text`, :meth:`~pyrogram.types.Message.translate` and the type :obj:`~pyrogram.types.TranslatedText` (`#39 <https://github.com/TelegramPlayGround/pyrogram/pull/39>`_).
- Added the methods :meth:`~pyrogram.Client.create_video_chat`, :meth:`~pyrogram.Client.discard_group_call`, :meth:`~pyrogram.Client.get_video_chat_rtmp_url` and the type :obj:`~pyrogram.types.RtmpUrl` (`#37 <https://github.com/TelegramPlayGround/pyrogram/pull/37>`_).
- Added :meth:`~Client.on_story` to listen to story updates.
- Ability to run in `replit` environment without creating `a deployment <https://ask.replit.com/t/pyrogram-network-issue/33679/46>`_. Set the environment variable ``PYROGRAM_REPLIT_NWTRAFIK_PORT`` value to ``5222`` if you want to connect to Production Telegram Servers, **OR** Set the environment variable ``PYROGRAM_REPLIT_WNTRAFIK_PORT`` value to ``5223`` if you want to connect to Test Telegram Servers, before starting the :obj:`~pyrogram.Client`.
- Added the :meth:`~pyrogram.Client.invite_group_call_participants` (`#35 <https://github.com/TelegramPlayGround/pyrogram/pull/35>`_).
- Added the types :obj:`~pyrogram.types.LabeledPrice`, :obj:`~pyrogram.types.OrderInfo`, :obj:`~pyrogram.types.PreCheckoutQuery`, :obj:`~pyrogram.types.ShippingAddress`, :obj:`~pyrogram.types.ShippingOption`, :obj:`~pyrogram.types.ShippingQuery` and :obj:`~pyrogram.types.SuccessfulPayment`.
- Added the ``successful_payment`` parameter to the :obj:`~pyrogram.types.Message`. Added the filter :obj:`~pyrogram.filters.successful_payment` to detect service messages of Successful Payment type.
- Added the methods :meth:`~pyrogram.Client.send_invoice`, :meth:`~pyrogram.Client.answer_pre_checkout_query` (:meth:`~pyrogram.types.PreCheckoutQuery.answer`), :meth:`~pyrogram.Client.answer_shipping_query` (:meth:`~pyrogram.types.ShippingQuery.answer`), :meth:`~pyrogram.Client.refund_star_payment` and :meth:`~pyrogram.Client.create_invoice_link`.
- Added the :meth:`~pyrogram.Client.send_web_app_custom_request`.
- Added the :meth:`~pyrogram.Client.search_public_messages_by_tag` and :meth:`~pyrogram.Client.count_public_messages_by_tag`.
- Added the ``fetch_replies`` parameter to :obj:`~pyrogram.Client`.
- Added the :meth:`~pyrogram.Client.get_message_effects`.
- Added the parameter ``message_effect_id`` to the methods :meth:`~pyrogram.Client.send_message`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_audio`, :meth:`~pyrogram.Client.send_document`, :meth:`~pyrogram.Client.send_sticker`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_voice`, :meth:`~pyrogram.Client.send_location`, :meth:`~pyrogram.Client.send_venue`, :meth:`~pyrogram.Client.send_contact`, :meth:`~pyrogram.Client.send_poll`, :meth:`~pyrogram.Client.send_dice`, :meth:`~pyrogram.Client.send_game`, and :meth:`~pyrogram.Client.send_media_group`, and the corresponding ``reply_*`` methods in the class :obj:`~pyrogram.types.Message`.
- Added the field ``effect_id`` to the class :obj:`~pyrogram.types.Message`.
- Added the field ``show_caption_above_media`` to the classes :obj:`~pyrogram.types.Message`, :obj:`~pyrogram.types.InputMediaAnimation`, :obj:`~pyrogram.types.InputMediaPhoto`, :obj:`~pyrogram.types.InputMediaVideo`, :obj:`~pyrogram.types.InlineQueryResultAnimation`, :obj:`~pyrogram.types.InlineQueryResultCachedAnimation`,  :obj:`~pyrogram.types.InlineQueryResultPhoto`, :obj:`~pyrogram.types.InlineQueryResultCachedPhoto`, :obj:`~pyrogram.types.InlineQueryResultVideo`, :obj:`~pyrogram.types.InlineQueryResultCachedVideo`, :meth:`~pyrogram.Client.send_cached_media`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.copy_message` and :meth:`~pyrogram.Client.edit_message_caption`, and the corresponding ``reply_*`` methods.
- Added support for :obj:`~pyrogram.enums.MessageEntityType.EXPANDABLE_BLOCKQUOTE` entities in received messages.
- Added support for :obj:`~pyrogram.enums.MessageEntityType.EXPANDABLE_BLOCKQUOTE` entity parsing in :obj:`~pyrogram.enums.ParseMode.HTML` parse mode.
- Allowed to explicitly specify :obj:`~pyrogram.enums.MessageEntityType.EXPANDABLE_BLOCKQUOTE` entities in formatted texts.
- `View new and changed raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop.html?from=178&to=181>`__.

+------------------------+
| Scheme layer used: 179 |
+------------------------+

- Add ``invoice`` to :obj:`~pyrogram.types.Message` and :obj:`~pyrogram.types.ExternalReplyInfo`.
- Add ``link_preview_options`` to :obj:`~pyrogram.Client`.
- Support for the updated Channel ID format. `#28 <https://github.com/TelegramPlayGround/pyrogram/pull/28>`_
- Improvements to :meth:`~pyrogram.Client.save_file` and :meth:`~pyrogram.Client.get_file` to handle the new `FLOOD_PREMIUM_WAIT <https://t.me/swiftgram/72>`_ errors.
- Added ``has_animation``, ``is_personal``, ``minithumbnail`` parameters to :obj:`~pyrogram.types.ChatPhoto`.
- Changed return type of :meth:`~pyrogram.Client.get_chat_photos` to return :obj:`~pyrogram.types.Photo` or :obj:`~pyrogram.types.Animation`.
- Added :meth:`~pyrogram.Client.get_chat_sponsored_messages` and the type :obj:`~pyrogram.types.SponsoredMessage`, by stealing unauthored changes from `KurimuzonAkuma/pyrogram#55 <https://github.com/KurimuzonAkuma/pyrogram/pull/55>`_.
- Added :meth:`~pyrogram.Client.load_group_call_participants` and the type :obj:`~pyrogram.types.GroupCallParticipant`, by stealing unauthored changes from `6df467f <https://github.com/KurimuzonAkuma/pyrogram/commit/6df467f89c0f6fa513a3f56ff1b517574fd3d164>`_.
- Added :meth:`~pyrogram.Client.view_messages` and the bound methods :meth:`~pyrogram.types.Message.read` and :meth:`~pyrogram.types.Message.view`.
- Added the field ``question_entities`` to the class :obj:`~pyrogram.types.Poll`.
- Added the field ``text_entities`` to the class :obj:`~pyrogram.types.PollOption`.
- Added the parameters ``question_parse_mode`` and ``question_entities`` to the method :meth:`~pyrogram.Client.send_poll`.
- Added the class :obj:`~pyrogram.types.InputPollOption` and changed the type of the parameter ``options`` in the method :meth:`~pyrogram.Client.send_poll` to Array of :obj:`~pyrogram.types.InputPollOption`.
- Added the field ``max_reaction_count`` to the class :obj:`~pyrogram.types.Chat`.
- Added the field ``via_join_request`` to the class :obj:`~pyrogram.types.ChatMemberUpdated`.
- Added the class :obj:`~pyrogram.types.TextQuote` and the field ``quote`` of type :obj:`~pyrogram.types.TextQuote` to the class :obj:`~pyrogram.types.Message`, which contains the part of the replied message text or caption that is quoted in the current message.
- Added ``full_name`` to :obj:`~pyrogram.types.Chat` and :obj:`~pyrogram.types.User` only for :obj:`~pyrogram.enums.ChatType.PRIVATE`.
- Added ``revoke_messages`` parameter to :meth:`~pyrogram.Client.ban_chat_member` and :meth:`~pyrogram.types.Chat.ban_member`.
- Added :meth:`~pyrogram.Client.get_collectible_item_info`.
- Added ``reverse`` parameter to :meth:`~pyrogram.Client.get_chat_history`. (`855e69e <https://github.com/pyrogram/pyrogram/blob/855e69e3f881c8140781c1d5e42e3098b2134dd2/pyrogram/methods/messages/get_history.py>`_, `a086b49 <https://github.com/dyanashek/pyrogram/commit/a086b492039687dd1b807969f9202061ce5305da>`_)
- `View new and changed raw API methods <https://telegramplayground.github.io/TG-APIs/TL/diff/tdesktop?from=176&to=178>`__.

+------------------------+
| Scheme layer used: 178 |
+------------------------+

- Added :meth:`~pyrogram.Client.search_chats`.
- Added :meth:`~pyrogram.Client.get_bot_name`, :meth:`~pyrogram.Client.get_bot_info_description`, :meth:`~pyrogram.Client.get_bot_info_short_description`, :meth:`~pyrogram.Client.set_bot_name`, :meth:`~pyrogram.Client.set_bot_info_description`, :meth:`~pyrogram.Client.set_bot_info_short_description`.
- Added :meth:`~pyrogram.Client.edit_cached_media` and :meth:`~pyrogram.types.Message.edit_cached_media`.
- Steal `d51eef3 <https://github.com/PyrogramMod/PyrogramMod/commit/d51eef31dc28724405ff473e45ca21b7d835d8b4>`_ without attribution.
- Added ``max_reaction_count`` to :obj:`~pyrogram.types.ChatReactions`.
- Added ``personal_chat_message`` to :obj:`~pyrogram.types.Chat`.
- Added ``only_in_channels`` parameter to :meth:`~pyrogram.Client.search_global` and :meth:`~pyrogram.Client.search_global_count`.

+------------------------+
| Scheme layer used: 177 |
+------------------------+

- Added ``emoji_message_interaction`` parameter to :meth:`~pyrogram.Client.send_chat_action` and :meth:`~pyrogram.types.Message.reply_chat_action`.
- **BOTS ONLY**: Updated :obj:`~pyrogram.handlers.ChatMemberUpdatedHandler` to handle updates when the bot is blocked or unblocked by a user.
- Added missing parameters in :meth:`~pyrogram.Client.create_group`, :meth:`~pyrogram.Client.create_supergroup`, :meth:`~pyrogram.Client.create_channel`.
- Try to return the service message (when applicable) in the methods :meth:`~pyrogram.Client.add_chat_members`, :meth:`~pyrogram.Client.promote_chat_member`
- Add :obj:`~pyrogram.enums.ChatAction.TRIGGER_EMOJI_ANIMATION` and :obj:`~pyrogram.enums.ChatAction.WATCH_EMOJI_ANIMATION` in :meth:`~pyrogram.Client.send_chat_action` and :meth:`~pyrogram.types.Message.reply_chat_action`.
- Attempted to revert the Backward Incompatible changes in the commits `fb118f95d <https://github.com/TelegramPlayGround/pyrogram/commit/fb118f9>`_ and `848bc8644 <https://github.com/TelegramPlayGround/pyrogram/commit/848bc86>`_.
- Added ``callback_data_with_password`` to :obj:`~pyrogram.types.InlineKeyboardButton` and added support in :meth:`~pyrogram.types.Message.click` for such buttons.
- PR from upstream: `1391 <https://github.com/pyrogram/pyrogram/pull/1391>`_ without attribution.
- Added ``gifted_premium`` service message to :obj:`~pyrogram.types.Message`.
- Added :meth:`~pyrogram.Client.get_stickers`.
- Added ``filters.users_shared`` and ``filters.chat_shared``.
- Added the field ``origin`` of type :obj:`~pyrogram.types.MessageOrigin` in the class :obj:`~pyrogram.types.ExternalReplyInfo`.
- Added the class :obj:`~pyrogram.types.MessageOrigin` and replaced the fields ``forward_from``, ``forward_from_chat``, ``forward_from_message_id``, ``forward_signature``, ``forward_sender_name``, and ``forward_date`` with the field ``forward_origin`` of type :obj:`~pyrogram.types.MessageOrigin` in the class :obj:`~pyrogram.types.Message`.
- Added ``accent_color``, ``profile_color``, ``emoji_status``, ``is_close_friend`` to :obj:`~pyrogram.types.Chat` and :obj:`~pyrogram.types.User`.
- Added the method :meth:`~pyrogram.Client.get_created_chats`.
- Added the class :obj:`~pyrogram.types.ForumTopic` and the methods :meth:`~pyrogram.Client.get_forum_topics`, :meth:`~pyrogram.Client.get_forum_topic`.
- Install the version, from PyPI, using ``pip uninstall -y pyrogram && pip install pyrotgfork==2.1.17``.
- Added the classes :obj:`~pyrogram.types.BusinessOpeningHours` and :obj:`~pyrogram.types.BusinessOpeningHoursInterval` and the field       ``business_opening_hours`` to the class :obj:`~pyrogram.types.Chat`.
- Added the class :obj:`~pyrogram.types.BusinessLocation` and the field ``business_location`` to the class :obj:`~pyrogram.types.Chat`.
- Added the class :obj:`~pyrogram.types.BusinessIntro` and the field ``business_intro`` to the class :obj:`~pyrogram.types.Chat`.
- Added the parameter ``business_connection_id`` to the methods :meth:`~pyrogram.Client.send_message`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_audio`, :meth:`~pyrogram.Client.send_document`, :meth:`~pyrogram.Client.send_sticker`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_voice`, :meth:`~pyrogram.Client.send_location`, :meth:`~pyrogram.Client.send_venue`, :meth:`~pyrogram.Client.send_contact`, :meth:`~pyrogram.Client.send_poll`, :meth:`~pyrogram.Client.send_game`, :meth:`~pyrogram.Client.send_media_group`, :meth:`~pyrogram.Client.send_dice`, :meth:`~pyrogram.Client.send_chat_action`, :meth:`~pyrogram.Client.send_cached_media` and :meth:`~pyrogram.Client.copy_message` and the corresponding reply_* methods.
- Added :meth:`~pyrogram.Client.get_business_connection`.
- Added ``active_usernames`` to :obj:`~pyrogram.types.Chat` and :obj:`~pyrogram.types.User`.
- Added :obj:`~pyrogram.types.BusinessConnection`.
- Added support for ``https://t.me/m/blah`` links in the ``link`` parameter of :meth:`~pyrogram.Client.get_messages`
- Added the parameter ``message_thread_id`` to the :meth:`~pyrogram.Client.search_messages` and :meth:`~pyrogram.Client.search_messages_count`.
- Added the parameter ``chat_list`` to :meth:`~pyrogram.Client.search_global` and :meth:`~pyrogram.Client.search_global_count`.
- **BOTS ONLY**: Handled the parameter ``business_connection_id`` to the update handlers :obj:`~pyrogram.handlers.MessageHandler`, :obj:`~pyrogram.handlers.EditedMessageHandler`, :obj:`~pyrogram.handlers.DeletedMessagesHandler`.
- Added the field ``business_connection_id`` to the class :obj:`~pyrogram.types.Message`.
- Bug fix for the ``users_shared``, ``chat_shared`` logic in :obj:`~pyrogram.types.Message`.
- Added :meth:`~pyrogram.Client.set_birthdate` and :meth:`~pyrogram.Client.set_personal_chat`, for user accounts only.
- Added the field ``birthdate`` to the class :obj:`~pyrogram.types.Chat`.
- Added the field ``is_from_offline`` to the class :obj:`~pyrogram.types.Message`.
- Added the field ``sender_business_bot`` to the class :obj:`~pyrogram.types.Message`.
- Added the fields ``users_shared``, ``chat_shared`` to the class :obj:`~pyrogram.types.Message`.
- Added the field ``personal_chat`` to the class :obj:`~pyrogram.types.Chat`.
- Added the field ``can_connect_to_business`` to the class :obj:`~pyrogram.types.User`.
- Rearrange :meth:`~pyrogram.Client.send_sticker` parameter names.
- Added the fields ``request_title``, ``request_username``, and ``request_photo`` to the class :obj:`~pyrogram.types.KeyboardButtonRequestChat`.
- Added the fields ``request_name``, ``request_username``, and ``request_photo`` to the class :obj:`~pyrogram.types.KeyboardButtonRequestUsers`.

+------------------------+
| Scheme layer used: 176 |
+------------------------+

- Add ``message_thread_id`` parameter to :meth:`~pyrogram.Client.unpin_all_chat_messages`.
- Add :meth:`~pyrogram.Client.create_forum_topic`, :meth:`~pyrogram.Client.edit_forum_topic`, :meth:`~pyrogram.Client.close_forum_topic`, :meth:`~pyrogram.Client.reopen_forum_topic`, :meth:`~pyrogram.Client.hide_forum_topic`, :meth:`~pyrogram.Client.unhide_forum_topic`, :meth:`~pyrogram.Client.delete_forum_topic`, :meth:`~pyrogram.Client.get_forum_topic_icon_stickers`.
- Add ``AioSQLiteStorage``, by stealing the following commits:
    - `fded06e <https://github.com/KurimuzonAkuma/pyrogram/commit/fded06e7bdf8bb591fb5857d0f126986ccf357c8>`_
- Add ``skip_updates`` parameter to :obj:`~pyrogram.Client` class, by stealing the following commits:
    - `c16c83a <https://github.com/KurimuzonAkuma/pyrogram/commit/c16c83abc307e4646df0eba34aad6de42517c8bb>`_
    - `55aa162 <https://github.com/KurimuzonAkuma/pyrogram/commit/55aa162a38831d79604d4c10df1a046c8a1c3ea6>`_
- Add ``public``, ``for_my_bot`` to :meth:`~pyrogram.Client.delete_profile_photos`.
- Make ``photo_ids`` parameter as optional in :meth:`~pyrogram.Client.delete_profile_photos`.
- Add ``supergroup_chat_created`` to :obj:`~pyrogram.types.Message`.
- Add ``forum_topic_created``, ``forum_topic_closed``, ``forum_topic_edited``, ``forum_topic_reopened``, ``general_forum_topic_hidden``, ``general_forum_topic_unhidden`` to :obj:`~pyrogram.types.Message`.
- Add ``custom_action`` to :obj:`~pyrogram.types.Message`.
- Add ``public``, ``for_my_bot``, ``photo_frame_start_timestamp`` to :meth:`~pyrogram.Client.set_profile_photo`.
- Add ``inline_need_location``, ``can_be_edited`` to :obj:`~pyrogram.types.User`.
- Add ``giveaway``, ``giveaway_created``, ``giveaway_completed`` and ``giveaway_winners`` in :obj:`~pyrogram.types.Message` and :obj:`~pyrogram.types.ExternalReplyInfo`.
- Bug fix for :meth:`~pyrogram.Client.send_message` with the ``message_thread_id`` parameter.
- Added ``request_users`` and ``request_chat`` to :obj:`~pyrogram.types.KeyboardButton`.
- **NOTE**: using the ``scheduled`` parameter, please be aware about using the correct :doc:`Message Identifiers <../../topics/message-identifiers>`.
    - Add ``is_scheduled`` parameter to :meth:`~pyrogram.Client.delete_messages`.
    - Add ``schedule_date`` parameter to :meth:`~pyrogram.Client.edit_message_caption`, :meth:`~pyrogram.Client.edit_message_media`, :meth:`~pyrogram.Client.edit_message_text`.
    - Added ``is_scheduled`` to :meth:`~pyrogram.Client.get_messages`.
    - Added ``is_scheduled`` to :meth:`~pyrogram.Client.get_chat_history`.
- Added new parameter ``client_platform`` to :obj:`~pyrogram.Client`.
- PR from upstream: `1403 <https://github.com/pyrogram/pyrogram/pull/1403>`_.
- Added ``story`` to :obj:`~pyrogram.types.ExternalReplyInfo`.
- Added ``story_id`` to :obj:`~pyrogram.types.ReplyParameters`.
- Added support for clicking (:obj:`~pyrogram.types.WebAppInfo`, :obj:`~pyrogram.types.LoginUrl`, ``user_id``, ``switch_inline_query_chosen_chat``) buttons in :meth:`~pyrogram.types.Message.click`.
- Rewrote :meth:`~pyrogram.Client.download_media` to support Story, and also made it future proof.
- `Fix bug in clicking UpdateBotCallbackQuery buttons <https://t.me/pyrogramchat/610636>`_

+-------------+
|  PmOItrOAe  |
+-------------+

- Renamed ``placeholder`` to ``input_field_placeholder`` in :obj:`~pyrogram.types.ForceReply` and :obj:`~pyrogram.types.ReplyKeyboardMarkup`.
- Add ``link`` parameter in :meth:`~pyrogram.Client.get_messages`
- `fix(filters): add type hints in filters.py <https://github.com/TelegramPlayGround/pyrogram/pull/8>`_
- Documentation Builder Fixes
- `faster-pyrogram <https://github.com/cavallium/faster-pyrogram>`__ is not polished or documented for anyone else's use. We don't have the capacity to support `faster-pyrogram <https://github.com/TelegramPlayGround/pyrogram/pull/6>`__ as an independent open-source project, nor any desire for it to become an alternative to Pyrogram. Our goal in making this code available is a unified faster Pyrogram. `... <https://github.com/cavallium/faster-pyrogram/blob/b781909/README.md#L28>`__

+-----------------------------+
|   Leaked Scheme Layers (2)  |
+-----------------------------+

- `Add ttl_seconds attribute to Voice and VideoNote class <https://github.com/KurimuzonAkuma/pyrogram/commit/7556d3e3864215386f018692947cdf52a82cb420>`_
- `#713 <https://github.com/pyrogram/pyrogram/pull/713>`_
- Removed :obj:`~pyrogram.types.ChatPreview` class, and merged the parameters with the :obj:`~pyrogram.types.Chat` class.
- Added ``description``, ``accent_color_id``, ``is_verified``, ``is_scam``, ``is_fake``, ``is_public``, ``join_by_request`` attributes to the class :obj:`~pyrogram.types.ChatPreview`.
- Added ``force_full`` parameter to :meth:`~pyrogram.Client.get_chat`.
- Bug Fix for :meth:`~pyrogram.Client.get_chat` and :meth:`~pyrogram.Client.join_chat` when ``https://t.me/username`` was passed.
- Added missing attributes to the class :obj:`~pyrogram.types.Story` when it is available.
- Added the field ``reply_to_story`` to the class :obj:`~pyrogram.types.Message`.
- Added the field ``user_chat_id`` to the class :obj:`~pyrogram.types.ChatJoinRequest`.
- Added the field ``switch_inline_query_chosen_chat`` of the type :obj:`~pyrogram.types.SwitchInlineQueryChosenChat` to the class :obj:`~pyrogram.types.InlineKeyboardButton`, which allows bots to switch to inline mode in a chosen chat of the given type.
- Add support for ``pay`` in :obj:`~pyrogram.types.InlineKeyboardButton`
- `#1345 <https://github.com/pyrogram/pyrogram/issues/1345>`_
- `Add undocumented things <https://github.com/TelegramPlayGround/pyrogram/commit/8a72939d98f343eae1e07981f95769efaa741e4e>`_
- `Add missing enums.SentCodeType <https://github.com/KurimuzonAkuma/pyrogram/commit/40ddcbca6062f13958f4ca2c9852f8d1c4d62f3c>`_
- `#693 <https://github.com/KurimuzonAkuma/pyrogram/pull/693>`_
- Revert `e678c05 <https://github.com/TelegramPlayGround/pyrogram/commit/e678c054d4aa0bbbb7d583eb426ca8753a4c9354>`_ and stole squashed unauthored changes from `bcd18d5 <https://github.com/Masterolic/pyrogram/commit/bcd18d5e04f18f949389a03f309816d6f0f9eabe>`_

+------------------------+
| Scheme layer used: 174 |
+------------------------+

- Added the field ``story`` to the class :obj:`~pyrogram.types.Message` for messages with forwarded stories. Currently, it holds no information.
- Added the class :obj:`~pyrogram.types.ChatBoostAdded` and the field ``boost_added`` to the class :obj:`~pyrogram.types.Message` for service messages about a user boosting a chat.
- Added the field ``custom_emoji_sticker_set_name`` to the class :obj:`~pyrogram.types.Chat`.
- Added the field ``unrestrict_boost_count`` to the class :obj:`~pyrogram.types.Chat`.
- Added the field ``sender_boost_count`` to the class :obj:`~pyrogram.types.Message`.

+------------------------+
| Scheme layer used: 173 |
+------------------------+

- Fix ConnectionResetError when only ping task (`#24 <https://github.com/KurimuzonAkuma/pyrogram/pull/24>`_)
- Added ``is_topic_message`` to the :obj:`~pyrogram.types.Message` object.
- Added ``has_visible_history``, ``has_hidden_members``, ``has_aggressive_anti_spam_enabled``, ``message_auto_delete_time``, ``slow_mode_delay``, ``slowmode_next_send_date``, ``is_forum`` to the :obj:`~pyrogram.types.Chat` object.
- Added ``add_to_recent``, ``story_id`` parameters in :meth:`~pyrogram.Client.set_reaction`.
- Bug fix in parsing ``Vector<Bool>`` (Thanks to `@AmarnathCJD <https://github.com/AmarnathCJD/>`_ and `@roj1512 <https://github.com/roj1512>`_).
- Documentation Fix of ``max_concurrent_transmissions`` type hint.
- Bug Fix in the ``get_file`` method. (Thanks to `@ALiwoto <https://github.com/ALiwoto>`_).
- Added missing attributes to :obj:`~pyrogram.types.ChatPermissions` and :obj:`~pyrogram.types.ChatPrivileges`.
- `Bug Fix for MIN_CHAT_ID <https://t.me/pyrogramchat/593090>`_.
- Added new parameter ``no_joined_notifications`` to :obj:`~pyrogram.Client`.
- Fix history TTL Service Message Parse.
- Thanks to `... <https://t.me/pyrogramchat/607757>`_. If you want to change the location of the ``unknown_errors.txt`` file that is created by :obj:`~pyrogram.Client`, set the environment variable ``PYROGRAM_LOG_UNKNOWN_ERRORS_FILENAME`` value to the path where the file should get created.
- Renamed ``force_document`` to ``disable_content_type_detection`` in :meth:`~pyrogram.Client.send_document` and :meth:`~pyrogram.types.Message.reply_document`.
- Added missing attributes ``added_to_attachment_menu``, ``can_be_added_to_attachment_menu``, ``can_join_groups``, ``can_read_all_group_messages``, ``supports_inline_queries``, ``restricts_new_chats`` to the :obj:`~pyrogram.types.User`.
- Migrate project to ``pyproject.toml`` from ``setup.py``.
- PRs from upstream: `1366 <https://github.com/pyrogram/pyrogram/pull/1366>`_, `1305 <https://github.com/pyrogram/pyrogram/pull/1305>`_, `1288 <https://github.com/pyrogram/pyrogram/pull/1288>`_, `1262 <https://github.com/pyrogram/pyrogram/pull/1262>`_, `1253 <https://github.com/pyrogram/pyrogram/pull/1253>`_, `1234 <https://github.com/pyrogram/pyrogram/pull/1234>`_, `1210 <https://github.com/pyrogram/pyrogram/pull/1210>`_, `1201 <https://github.com/pyrogram/pyrogram/pull/1201>`_, `1197 <https://github.com/pyrogram/pyrogram/pull/1197>`_, `1143 <https://github.com/pyrogram/pyrogram/pull/1143>`_, `1059 <https://github.com/pyrogram/pyrogram/pull/1059>`_.
- Bug fix for :meth:`~pyrogram.Client.send_audio` and :meth:`~pyrogram.Client.send_voice`. (Thanks to `... <https://t.me/c/1220993104/1360174>`_).
- Add `waveform` parameter to :meth:`~pyrogram.Client.send_voice`.
- Added `view_once` parameter to :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_voice`.
- Add missing parameters to :meth:`~pyrogram.types.Message.reply_photo`, :meth:`~pyrogram.types.Message.reply_video`, :meth:`~pyrogram.types.Message.reply_video_note`, :meth:`~pyrogram.types.Message.reply_voice`.

+------------------------+
| Scheme layer used: 170 |
+------------------------+

- Stole documentation from `PyrogramMod <https://github.com/PyrogramMod/PyrogramMod>`_.
- Renamed ``send_reaction`` to :meth:`~pyrogram.Client.set_reaction`.
- Added support for :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_voice` messages that could be played once.
- Added the field ``via_chat_folder_invite_link`` to the class :obj:`~pyrogram.types.ChatMemberUpdated`.
- **BOTS ONLY**: Added updates about a reaction change on a message with non-anonymous reactions, represented by the class :obj:`~pyrogram.handlers.MessageReactionUpdatedHandler` and the field ``message_reaction`` in the class Update.
- **BOTS ONLY**: Added updates about reaction changes on a message with anonymous reactions, represented by the class :obj:`~pyrogram.handlers.MessageReactionCountUpdatedHandler` and the field ``message_reaction_count`` in the class Update.
- Replaced the parameter ``disable_web_page_preview`` with :obj:`~pyrogram.types.LinkPreviewOptions` in the methods :meth:`~pyrogram.Client.send_message` and :meth:`~pyrogram.Client.edit_message_text`.
- Replaced the field ``disable_web_page_preview`` with :obj:`~pyrogram.types.LinkPreviewOptions` in the class :obj:`~pyrogram.types.InputTextMessageContent`.
- Added missing parameters to :meth:`~pyrogram.Client.forward_messages`.
- Added the class :obj:`~pyrogram.types.ReplyParameters` and replaced parameters ``reply_to_message_id`` in the methods :meth:`~pyrogram.Client.copy_message`, :meth:`~pyrogram.Client.send_message`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_audio`, :meth:`~pyrogram.Client.send_document`, :meth:`~pyrogram.Client.send_sticker`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_voice`, :meth:`~pyrogram.Client.send_location`, :meth:`~pyrogram.Client.send_venue`, :meth:`~pyrogram.Client.send_contact`, :meth:`~pyrogram.Client.send_poll`, :meth:`~pyrogram.Client.send_dice`, :meth:`~pyrogram.Client.send_game`, :meth:`~pyrogram.Client.send_media_group`, :meth:`~pyrogram.Client.copy_media_group`, :meth:`~pyrogram.Client.send_inline_bot_result`, :meth:`~pyrogram.Client.send_cached_media`, and the corresponding reply_* methods with the field ``reply_parameters`` of type :obj:`~pyrogram.types.ReplyParameters`.
- Bug fixes for sending ``ttl_seconds`` and ``has_spoiler``.

+------------------------+
| Scheme layer used: 169 |
+------------------------+

- Changed condition in :meth:`~pyrogram.Client.join_chat` and :meth:`~pyrogram.Client.get_chat`.
- Added ``disable_content_type_detection`` parameter to :obj:`~pyrogram.types.InputMediaVideo`.
- Added ``has_spoiler`` parameter to :meth:`~pyrogram.Client.copy_message`.
- Improved :meth:`~pyrogram.Client.get_chat_history`: add ``min_id`` and ``max_id`` params.
- `Prevent connection to dc every time in get_file <https://github.com/TelegramPlayGround/pyrogram/commit/f2581fd7ab84ada7685645a6f80475fbea5e743a>`_
- Added ``_raw`` to the :obj:`~pyrogram.types.Chat`, :obj:`~pyrogram.types.Dialog`, :obj:`~pyrogram.types.Message` and :obj:`~pyrogram.types.User` objects.
- Fix downloading media to ``WORKDIR`` when ``WORKDIR`` was not specified.
- `Update multiple fragment chat usernames <https://github.com/TelegramPlayGround/pyrogram/commit/39aea4831ee18e5263bf6755306f0ca49f075bda>`_
- `Custom Storage Engines <https://github.com/TelegramPlayGround/pyrogram/commit/cd937fff623759dcac8f437a8c524684868590a4>`_
- Documentation fix for ``user.mention`` in :obj:`~pyrogram.types.User`.

+------------------------+
| Scheme layer used: 167 |
+------------------------+

- Fixed the TL flags being Python reserved keywords: ``from`` and ``self``.

+------------------------+
| Scheme layer used: 161 |
+------------------------+

- Added ``my_stories_from`` to the :meth:`~pyrogram.Client.block_user` and :meth:`~pyrogram.Client.unblock_user` methods.

+------------------------+
| Scheme layer used: 160 |
+------------------------+

- Added ``message_thread_id`` to the methods :meth:`~pyrogram.Client.copy_message`, :meth:`~pyrogram.Client.forward_messages`, :meth:`~pyrogram.Client.send_message`, :meth:`~pyrogram.Client.send_photo`, :meth:`~pyrogram.Client.send_video`, :meth:`~pyrogram.Client.send_animation`, :meth:`~pyrogram.Client.send_audio`, :meth:`~pyrogram.Client.send_document`, :meth:`~pyrogram.Client.send_sticker`, :meth:`~pyrogram.Client.send_video_note`, :meth:`~pyrogram.Client.send_voice`, :meth:`~pyrogram.Client.send_location`, :meth:`~pyrogram.Client.send_venue`, :meth:`~pyrogram.Client.send_contact`, :meth:`~pyrogram.Client.send_poll`, :meth:`~pyrogram.Client.send_dice`, :meth:`~pyrogram.Client.send_game`, :meth:`~pyrogram.Client.send_media_group`, :meth:`~pyrogram.Client.copy_media_group`, :meth:`~pyrogram.Client.send_inline_bot_result`, :meth:`~pyrogram.Client.send_cached_media`.
