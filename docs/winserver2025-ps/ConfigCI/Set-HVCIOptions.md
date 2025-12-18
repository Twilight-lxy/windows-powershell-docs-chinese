---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.ConfigCI.Commands.dll-Help.xml
Module Name: ConfigCI
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/configci/set-hvcioptions?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-HVCIOptions
---

# 设置 HVCI 选项

## 摘要
修改策略中的管理程序代码完整性（Code Integrity）相关选项。

## 语法

### 选项
```
Set-HVCIOptions [-Enabled] [-Strict] [-DebugMode] [-DisableAllowed] [-FilePath] <String> [<CommonParameters>]
```

### 无
```
Set-HVCIOptions [-None] [-FilePath] <String> [<CommonParameters>]
```

## 描述
`Set-HVCIOptions` cmdlet 用于修改与策略相关的虚拟机监控程序（hypervisor）代码完整性（Code Integrity）设置。这些设置会被存储在策略的 `HvciOptions` 属性中。你可以指定以下值的任意组合：

- Enabled
- DebugMode
- Strict

## 示例

### Example 1: Assign the Strict option
```
PS C:\> Set-HVCIOptions -Strict -FilePath '.\Policy.xml'
PS C:\> Get-Content -Path '.Policy.xml'
    <CiSigner SignerId="ID_SIGNER_S_21" />
  </CiSigners>
  <HvciOptions>2</HvciOptions>
</SiPolicy>
```

The first command assigns the Strict option in Policy.xml.

The second command displays the contents of the policy.
This example shows the last few lines of the policy, which include the **HvciOptions** property.
It now has a value of 2.

## 参数

### -DebugMode
Indicates that this cmdlet turns on DebugMode in the policy.

```yaml
Type: SwitchParameter
Parameter Sets: Options
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -DisableAllowed
Indicates that this cmdlet allows for HVCI to be disabled by the user outside of the Code Integrity policy enablement method.

```yaml
Type: SwitchParameter
Parameter Sets: Options
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Enabled
Indicates that this cmdlet turns on Enabled in the policy.

```yaml
Type: SwitchParameter
Parameter Sets: Options
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -FilePath
Specifies the path of the policy .xml file that this cmdlet modifies.

```yaml
Type: String
Parameter Sets: (All)
Aliases: f

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -None
Indicates that this cmdlet removes all hypervisor Code Integrity options from the policy.
In the policy itself, **HvciOptions** takes a value of zero (0).

```yaml
Type: SwitchParameter
Parameter Sets: None
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Strict
Indicates that this cmdlet turns on Strict in the policy.

```yaml
Type: SwitchParameter
Parameter Sets: Options
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Set-RuleOption](./Set-RuleOption.md)

