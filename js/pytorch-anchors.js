window.catalystAnchors = {
  bind: function() {
    // Replace Sphinx-generated anchors with anchorjs ones
    $(".headerlink").text("");

    window.anchors.add(".catalyst-article .headerlink");

    $(".anchorjs-link").each(function() {
      var $headerLink = $(this).closest(".headerlink");
      var href = $headerLink.attr("href");
      var clone = this.outerHTML;

      $clone = $(clone).attr("href", href);
      $headerLink.before($clone);
      $headerLink.remove();
    });
  }
};
