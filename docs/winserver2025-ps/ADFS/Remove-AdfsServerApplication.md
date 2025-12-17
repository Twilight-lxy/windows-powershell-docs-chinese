---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsserverapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsServerApplication
---

# 删除 AdfsServerApplication

## 摘要
从 AD FS 中的应用程序中删除一个服务器应用程序角色。

## 语法

### 标识符（默认值）
```
Remove-AdfsServerApplication [-TargetIdentifier] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 名称
```
Remove-AdfsServerApplication [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ApplicationObject
```
Remove-AdfsServerApplication [-TargetApplication] <ServerApplication> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsServerApplication` cmdlet 用于从 Active Directory Federation Services (AD FS) 中的某个应用程序中删除服务器应用程序角色。

## 示例

## 参数

### -PassThru
返回一个表示您正在操作的项目的对象。默认情况下，此cmdlet不会生成任何输出。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -TargetApplication
指定要卸载的服务器应用程序。

```yaml
Type: ServerApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要删除的服务器应用程序的ID。

```yaml
Type: String
Parameter Sets: Identifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName, ByValue)
Accept wildcard characters: False
```

### -TargetName
指定要删除的服务器应用程序的名称。

```yaml
Type: String
Parameter Sets: Name
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行该 cmdlet 之前，会提示您确认是否要执行此操作。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: cf

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果运行该cmdlet会发生什么情况。但实际上该cmdlet并没有被执行。

```yaml
Type: SwitchParameter
Parameter Sets: (All)
Aliases: wi

Required: False
Position: Named
Default value: False
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

## 输出

## 备注

## 相关链接

[Add-AdfsServerApplication](./Add-AdfsServerApplication.md)

[Get-AdfsServerApplication](./Get-AdfsServerApplication.md)

[Set-AdfsServerApplication](./Set-AdfsServerApplication.md)

