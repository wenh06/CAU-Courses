document.addEventListener("DOMContentLoaded", function () {
  const proofTitles = document.querySelectorAll(".proof .proof-title");

  // 遍历每个 proof 环境
  proofTitles.forEach((title) => {
    const content = title.nextElementSibling;
    const parent = title.closest(".proof");
    const typeClass = Array.from(parent.classList).find((c) =>
      c.startsWith("proof-type-")
    );
    const type = typeClass ? typeClass.replace("proof-type-", "") : "";

    // 默认展开或折叠逻辑
    const shouldCollapse = ["proof", "solution"].includes(type);

    if (shouldCollapse) {
      title.classList.remove("open");
      content.classList.remove("expanded");
      content.classList.add("collapsed");
    } else {
      title.classList.add("open");
      content.classList.add("expanded");
      content.classList.remove("collapsed");
    }

    // 点击切换展开/折叠
    title.addEventListener("click", function () {
      const isExpanded = content.classList.contains("expanded");

      if (isExpanded) {
        content.classList.remove("expanded");
        content.classList.add("collapsed");
        title.classList.remove("open");
      } else {
        content.classList.remove("collapsed");
        content.classList.add("expanded");
        title.classList.add("open");
      }

      // 更新顶部按钮状态
      updateToggleButtonState();
    });
  });

  // 兼容 Font Awesome SVG+JS，把 <i> 转成 <svg>
  function i2svg(node) {
    try {
      if (window.FontAwesome && FontAwesome.dom && typeof FontAwesome.dom.i2svg === "function") {
        FontAwesome.dom.i2svg({ node });
      }
    } catch (e) {}
  }

  function setToggleIcon(btn, expanded) {
    btn.innerHTML = expanded
      ? '<i class="proof-toggle-icon fa-solid fa-eye fa-lg" aria-hidden="true"></i>'
      : '<i class="proof-toggle-icon fa-solid fa-eye-slash fa-lg" aria-hidden="true"></i>';
    i2svg(btn);
  }

  // 只用 Bootstrap 的 data-bs-title，不用原生 title，避免第二个气泡
  function setTooltipText(btn, text) {
    btn.removeAttribute("title");
    btn.removeAttribute("data-bs-original-title");
    btn.setAttribute("data-bs-title", text);

    const inst = (window.bootstrap && bootstrap.Tooltip && bootstrap.Tooltip.getInstance)
      ? bootstrap.Tooltip.getInstance(btn)
      : null;

    // Bootstrap 5.2+ 动态更新内容
    if (inst && typeof inst.setContent === "function") {
      inst.setContent({ ".tooltip-inner": text });
      inst.update && inst.update();
    } else if (inst) {
      // 老版本：销毁后按最新 data-bs-title 重建
      inst.dispose();
      initTooltip(btn);
    }
  }

  function initTooltip(btn) {
    try {
      if (window.bootstrap && bootstrap.Tooltip) {
        const opts = { trigger: "hover", placement: "bottom", container: "body" };
        if (typeof bootstrap.Tooltip.getOrCreateInstance === "function") {
          return bootstrap.Tooltip.getOrCreateInstance(btn, opts);
        } else {
          return new bootstrap.Tooltip(btn, opts);
        }
      }
    } catch (e) {}
    return null;
  }

  // 创建折叠/展开图标按钮（主题样式 + Bootstrap tooltip）
  function createToggleButton() {
    const btn = document.createElement("button");
    btn.id = "proof-toggle-all";
    btn.className = "btn btn-sm nav-link pst-navbar-icon expanded";
    btn.type = "button";
    btn.setAttribute("data-bs-toggle", "tooltip");
    btn.setAttribute("data-bs-trigger", "hover");
    btn.setAttribute("data-bs-placement", "bottom");
    // 初始设为“收起”图标和文案，插入后会再用实际状态校正
    setToggleIcon(btn, true);
    setTooltipText(btn, "全部收起");
    initTooltip(btn);

    btn.addEventListener("click", function () {
      const contents = document.querySelectorAll(".proof-content");
      const titles = document.querySelectorAll(".proof .proof-title");
      const isExpanded = btn.classList.contains("expanded");

      if (isExpanded) {
        // 切换到全部收起
        contents.forEach((c) => {
          c.classList.remove("expanded");
          c.classList.add("collapsed");
        });
        titles.forEach((t) => t.classList.remove("open"));
        btn.classList.remove("expanded");
        btn.classList.add("collapsed");
        setToggleIcon(btn, false);
        setTooltipText(btn, "全部展开");
      } else {
        // 切换到全部展开
        contents.forEach((c) => {
          c.classList.add("expanded");
          c.classList.remove("collapsed");
        });
        titles.forEach((t) => t.classList.add("open"));
        btn.classList.remove("collapsed");
        btn.classList.add("expanded");
        setToggleIcon(btn, true);
        setTooltipText(btn, "全部收起");
      }

      // 防粘住：点击后隐藏 tooltip 并移除焦点
      try {
        const inst = bootstrap.Tooltip.getInstance(btn);
        inst && inst.hide();
      } catch (e) {}
      btn.blur();
    });

    // 再保险：鼠标离开时，如果仍因焦点残留可见，则隐藏
    btn.addEventListener("mouseleave", function () {
      try {
        const inst = bootstrap.Tooltip.getInstance(btn);
        if (inst && document.activeElement === btn) {
          inst.hide();
          btn.blur();
        }
      } catch (e) {}
    });

    return btn;
  }

  // 更新按钮状态（当手动切换单个 proof 时）
  function updateToggleButtonState() {
    const btn = document.getElementById("proof-toggle-all");
    if (!btn) return;

    const expandedProofs = document.querySelectorAll(".proof-content.expanded").length;
    const totalProofs = document.querySelectorAll(".proof-content").length;

    if (totalProofs === 0) {
      btn.classList.remove("collapsed");
      btn.classList.add("expanded");
      setToggleIcon(btn, true);
      setTooltipText(btn, "全部收起");
      return;
    }

    if (expandedProofs === totalProofs) {
      btn.classList.remove("collapsed");
      btn.classList.add("expanded");
      setToggleIcon(btn, true);
      setTooltipText(btn, "全部收起");
    } else if (expandedProofs === 0) {
      btn.classList.remove("expanded");
      btn.classList.add("collapsed");
      setToggleIcon(btn, false);
      setTooltipText(btn, "全部展开");
    } else {
      if (expandedProofs >= totalProofs / 2) {
        btn.classList.remove("collapsed");
        btn.classList.add("expanded");
        setToggleIcon(btn, true);
        setTooltipText(btn, "全部收起");
      } else {
        btn.classList.remove("expanded");
        btn.classList.add("collapsed");
        setToggleIcon(btn, false);
        setTooltipText(btn, "全部展开");
      }
    }
  }

  // 插入按钮到工具栏（放最左侧，融入主题 DOM 结构）
  function insertToggleButton() {
    const toolbarSelectors = [
      ".header-article-items__end",
      ".header-article__right",
      ".bd-header__right",
      ".navbar-header-items__end",
      ".bd-header-article__inner .bd-header-article__buttons"
    ];

    let toolbar = null;
    for (const selector of toolbarSelectors) {
      toolbar = document.querySelector(selector);
      if (toolbar) break;
    }

    if (toolbar) {
      const btn = createToggleButton();

      // 放到现有 .header-article-item .article-header-buttons 的最左侧
      let articleButtons = toolbar.querySelector(".header-article-item .article-header-buttons");
      if (articleButtons) {
        articleButtons.prepend(btn);
      } else {
        // 若无该结构，创建并插在 toolbar 最左侧
        const wrapper = document.createElement("div");
        wrapper.className = "header-article-item";
        const buttons = document.createElement("div");
        buttons.className = "article-header-buttons";
        buttons.appendChild(btn);
        wrapper.appendChild(buttons);
        toolbar.insertBefore(wrapper, toolbar.firstChild);
      }

      // 初始根据页面实际状态校正图标与 tooltip 文案
      updateToggleButtonState();
    } else {
      console.warn("Proof: 未找到工具栏位置，折叠/展开按钮未插入");
    }
  }

  insertToggleButton();
});
