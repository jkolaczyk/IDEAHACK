import React from "react";
import Tags from "@yaireo/tagify/dist/react.tagify";
import "@yaireo/tagify/dist/tagify.css" // Tagify CSS


const baseTagifySettings = {
    blacklist: [],
    maxTags: 15,
    backspace: "edit",
    placeholder: "Input skills",
    editTags: 1,
    dropdown: {
        enabled: 0
    },
    callbacks: {}
};

function TagField({ label, name, initialValue = [], suggestions = [], setTags }) {
    const handleChange = e => {
        // console.log(e.type, " ==> ", e.detail.tagify.value.map(item => item.value));
        setTags(e.detail.tagify.value.map(item => item.value))
    };

    const settings = {
        ...baseTagifySettings,
        whitelist: suggestions,
        enforceWhitelist: true,
        callbacks: {
            add: handleChange,
            remove: handleChange,
            blur: handleChange,
            edit: handleChange,
            invalid: handleChange,
            click: handleChange,
            focus: handleChange,
            "edit:updated": handleChange,
            "edit:start": handleChange
        }
    };

    return (
        <div className="form-group">
            <label htmlFor={"field-" + name}>{label}</label>
            <Tags settings={settings} initialValue={initialValue} />
        </div>
    );
}

export default TagField