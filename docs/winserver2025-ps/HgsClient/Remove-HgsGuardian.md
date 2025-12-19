---
description: 使用此主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: HgsClient-help.xml
Module Name: HgsClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsclient/remove-hgsguardian?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-HgsGuardian
---

# 移除 HgsGuardian

## 摘要
从守护者商店中移除一个守护者。

## 语法

### NameViaString（默认值）
```
Remove-HgsGuardian [-Name] <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 名称：ViaGuardian
```
Remove-HgsGuardian [-InputObject] <CimInstance> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-HgsGuardian` cmdlet 用于从守护程序存储中删除一个 Host Guardian Service 的守护对象。

## 示例

### 示例 1：移除守护者
```
PS C:\> Remove-HgsGuardian -Name "Guardian11"
```

此命令会将名为 Guardian11 的守护程序从本地存储中删除。

## 参数

### -InputObject
需要移除的HGS守护对象。

```yaml
Type: CimInstance
Parameter Sets: NameViaGuardian
Aliases: Guardian

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Name
指定要移除的监护人的名称。

```yaml
Type: String
Parameter Sets: NameViaString
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前，会提示您确认是否要继续执行该操作。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被运行。

```yaml
Type: System.Management.Automation.SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于COMMONPARAMETERS（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

## 备注

## 相关链接

[Export-HgsGuardian](./Export-HgsGuardian.md)

[Get-HgsGuardian](./Get-HgsGuardian.md)

[Import-HgsGuardian](./Import-HgsGuardian.md)

[New-HgsGuardian](./New-HgsGuardian.md)

