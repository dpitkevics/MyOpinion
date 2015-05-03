$(function () {
    //var hash = window.location.hash;
    //
    //var hashObj = $(hash);
    //if (!hashObj.hasClass('comment-form')) {
    //    $(hash).addClass('comment-active');
    //}
});

function setReplyTo(replyButton)
{
    replyButton.html('<span class="glyphicon glyphicon-remove"></span> Do not Reply');
    replyButton.attr("onclick", "return removeReply($(this));");

    var commentId = replyButton.parents('.comment-row').attr('id');

    var activeComment = $(".comment-active");

    if (activeComment.length > 0) {
        removeReply(activeComment.find('.reply-btn'));
    }

    activeComment.removeClass('comment-active');
    $("#" + commentId).addClass('comment-active');

    window.location.hash = "comment";

    var commentForm = $("#comment-form");
    var replyToInput = commentForm.find("input#reply_to");

    if (replyToInput.length == 1) {
        replyToInput.val(commentId);

        makeCommentLabel(commentForm, commentId);
    } else if (replyToInput.length == 0) {
        replyToInput = $('<input type="hidden" name="reply_to" id="reply_to" value="'+commentId+'" />');
        commentForm.prepend(replyToInput);

        makeCommentLabel(commentForm, commentId);
    }

    return false;
}

function removeReply(replyButton)
{
    replyButton.html('<span class="glyphicon glyphicon-share-alt"></span> Reply');
    replyButton.attr("onclick", "return setReplyTo($(this));");

    var commentId = replyButton.parents('.comment-row').attr('id');

    $(".comment-active").removeClass('comment-active');

    var commentForm = $("#comment-form");
    var replyToInput = commentForm.find("input#reply_to");

    replyToInput.remove();

    removeCommentLabel();

    return false;
}

function makeCommentLabel(commentForm, commentId)
{
    removeCommentLabel();

    var label = $('<span class="label label-info">You are replying to a comment. Click to see it.</span>');
    var link = $('<a href="#'+commentId+'" id="reply-to-label"></a>');

    link.append(label);
    commentForm.prepend(link);
}

function removeCommentLabel()
{
    var existingLabel = $("#reply-to-label");
    if (existingLabel.length > 0) {
        existingLabel.remove();
    }
}