#!/usr/bin/env python3
"""Test script for LTX Director core functions (without torch dependency)."""

import json
import sys


def _calculate_required_duration(timeline_data_str: str) -> int:
    """Calculate minimum required timeline duration."""
    if not timeline_data_str:
        return 1
    try:
        data = json.loads(timeline_data_str)
    except Exception:
        return 1
    max_end = 1
    for seg in data.get("segments", []):
        seg_end = int(seg.get("start", 0)) + int(seg.get("length", 1))
        max_end = max(max_end, seg_end)
    for seg in data.get("audioSegments", []):
        seg_end = int(seg.get("start", 0)) + int(seg.get("length", 1))
        max_end = max(max_end, seg_end)
    return max_end


def _validate_audio_segments(timeline_data_str: str, frame_rate: float) -> dict:
    """Validate all audio segments."""
    result = {"valid": True, "warnings": [], "segments_info": []}
    if not timeline_data_str:
        return result
    try:
        data = json.loads(timeline_data_str)
    except Exception:
        return result
    for seg in data.get("audioSegments", []):
        info = {
            "id": seg.get("id"),
            "trim_start": seg.get("trimStart", 0),
            "length_frames": seg.get("length", 1),
            "source_duration": seg.get("audioDurationFrames", 0)
        }
        trim_end = info["trim_start"] + info["length_frames"]
        if trim_end > info["source_duration"]:
            result["warnings"].append(f"Audio {info['id']}: trim {trim_end} > source {info['source_duration']}")
        result["segments_info"].append(info)
    return result


def _align_image_audio(timeline_data_str: str, tolerance_frames: int = 6) -> dict:
    """Check image-audio alignment."""
    alignment_info = {"pairs": [], "misalignments": []}
    if not timeline_data_str:
        return alignment_info
    try:
        data = json.loads(timeline_data_str)
    except Exception:
        return alignment_info
    for img in data.get("segments", []):
        img_start, img_end = img.get("start", 0), img.get("start", 0) + img.get("length", 1)
        matching = []
        for aud in data.get("audioSegments", []):
            aud_start, aud_end = aud.get("start", 0), aud.get("start", 0) + aud.get("length", 1)
            if img_start < aud_end and img_end > aud_start:
                offset = aud_start - img_start
                matching.append({"audio_id": aud.get("id"), "offset": offset, "aligned": abs(offset) < tolerance_frames})
        if matching:
            alignment_info["pairs"].append({"image_id": img.get("id"), "audio": matching})
            unaligned = [a for a in matching if not a["aligned"]]
            if unaligned:
                alignment_info["misalignments"].append({"image_id": img.get("id"), "issues": unaligned})
    return alignment_info


def test_duration():
    """Test duration calculation."""
    print("Testing duration calculation...")
    assert _calculate_required_duration("") == 1
    assert _calculate_required_duration(json.dumps({"segments": [{"start": 0, "length": 48}]})) == 48
    assert _calculate_required_duration(json.dumps({"audioSegments": [{"start": 0, "length": 120}]})) == 120
    print("  ✅ All duration tests passed")


def test_audio():
    """Test audio validation."""
    print("Testing audio validation...")
    result = _validate_audio_segments(json.dumps({"audioSegments": [{"id": "a1", "trimStart": 0, "length": 48, "audioDurationFrames": 100}]}), 24.0)
    assert len(result["warnings"]) == 0
    result = _validate_audio_segments(json.dumps({"audioSegments": [{"id": "a1", "trimStart": 50, "length": 100, "audioDurationFrames": 100}]}), 24.0)
    assert len(result["warnings"]) > 0
    print("  ✅ All audio tests passed")


def test_alignment():
    """Test image-audio alignment."""
    print("Testing alignment...")
    result = _align_image_audio(json.dumps({
        "segments": [{"id": "img1", "start": 0, "length": 48}],
        "audioSegments": [{"id": "aud1", "start": 0, "length": 48}]
    }), tolerance_frames=6)
    assert len(result["misalignments"]) == 0
    result = _align_image_audio(json.dumps({
        "segments": [{"id": "img1", "start": 0, "length": 48}],
        "audioSegments": [{"id": "aud1", "start": 20, "length": 48}]
    }), tolerance_frames=6)
    assert len(result["misalignments"]) > 0
    print("  ✅ All alignment tests passed")


if __name__ == "__main__":
    try:
        test_duration()
        test_audio()
        test_alignment()
        print("\n✅ All tests passed!")
    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Error: {e}")
        sys.exit(1)
