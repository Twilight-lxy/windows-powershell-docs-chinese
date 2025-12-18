---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/set-ruleoption?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-RuleOption
---

# Set-RuleOption

## 摘要
修改代码完整性策略中的规则选项。

## 语法

### 行动
```
Set-RuleOption [-Delete] [-FilePath] <String> [-Option] <Int32> [<CommonParameters>]
```

### 帮助
```
Set-RuleOption [-Help] [<CommonParameters>]
```

## 描述
`Set-RuleOption` cmdlet 用于修改代码完整性策略中的规则选项。这些规则选项位于 `.xml` 策略文件中的 `Rules` 属性下。要查看可用的规则选项及其索引，请指定 `Help` 参数。该 cmdlet 可根据您指定的索引来添加相应的规则选项；如果要删除某个规则选项，则需要指定 `Delete` 参数。

## 示例

### 示例 1：移除某个规则选项
```
The first command displays the contents of the policy. This example shows only the first few lines of the policy, which include the **Rules** property. One of the options displayed is Enabled:Audit Mode.
PS C:\> Get-Content -Path '.Policy.xml'
<?xml version="1.0" encoding="utf-8"?>
<SiPolicy xmlns="urn:schemas-microsoft-com:sipolicy">
  <VersionEx>10.0.0.0</VersionEx>
  <PolicyTypeID>{A244370E-44C9-4C06-B551-F6016E563076}</PolicyTypeID>
  <PlatformID>{2E07F7E4-194C-4D20-B7C9-6F44A6C5A234}</PlatformID>
  <Rules>
    <Rule>
      <Option>Enabled:Unsigned System Integrity Policy</Option>
    </Rule>
    <Rule>
      <Option>Enabled:Audit Mode</Option>
    </Rule>
    <Rule>
      <Option>Enabled:Advanced Boot Options Menu</Option>
    </Rule>
    <Rule>
      <Option>Enabled:UMCI</Option>
    </Rule>
  </Rules>

The second command removes the Enabled:Audit Mode from Policy.xml.The final command displays the contents of the policy again. Enabled:Audit Mode is no longer part of the policy.
PS C:\> Set-RuleOption -FilePath '.\Policy.xml' -Option 3 -Delete
PS C:\> Get-Content -Path '.Policy.xml'
<?xml version="1.0" encoding="utf-8"?>
<SiPolicy xmlns="urn:schemas-microsoft-com:sipolicy">
  <VersionEx>10.0.0.0</VersionEx>
  <PolicyTypeID>{A244370E-44C9-4C06-B551-F6016E563076}</PolicyTypeID>
  <PlatformID>{2E07F7E4-194C-4D20-B7C9-6F44A6C5A234}</PlatformID>
  <Rules>
    <Rule>
      <Option>Enabled:Unsigned System Integrity Policy</Option>
    </Rule>
    <Rule>
      <Option>Enabled:Advanced Boot Options Menu</Option>
    </Rule>
    <Rule>
      <Option>Enabled:UMCI</Option>
    </Rule>
  </Rules>
```

这个示例从策略中删除了“Enabled:Audit Mode”这一选项。

## 参数

### -Delete
表示此cmdlet会删除由`Option`参数指定的规则选项。

```yaml
Type: SwitchParameter
Parameter Sets: Action
Aliases: d

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath
指定此cmdlet所修改的policy.xml文件的路径。

```yaml
Type: String
Parameter Sets: Action
Aliases: f

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Help
表示此 cmdlet 会显示可用选项及其索引的列表。

```yaml
Type: SwitchParameter
Parameter Sets: Help
Aliases: h

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Option
指定此 cmdlet 所修改的规则选项的索引。若需了解有关选项的信息，请使用 **Help** 参数。有关每个选项的更详细描述，请参阅 [WDAC 策略规则选项](/windows/security/threat-protection/windows-defender-application-control/select-types-of-rules-to-create#windows-defender-application-control-policy-rules)。

```yaml
Type: Int32
Parameter Sets: Action
Aliases: o

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about	CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-HVCIOptions](./Set-HVCIOptions.md)
