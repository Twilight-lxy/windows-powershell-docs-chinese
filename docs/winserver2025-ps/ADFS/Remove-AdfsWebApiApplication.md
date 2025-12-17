---
description: 使用这个主题来帮助通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfswebapiapplication?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsWebApiApplication
---

# 移除 AdfsWebApi 应用程序

## 摘要
从AD FS中的某个应用程序中删除Web API应用程序角色。

## 语法

### 标识符（默认值）
```
Remove-AdfsWebApiApplication [-TargetIdentifier] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 名称
```
Remove-AdfsWebApiApplication [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ApplicationObject
```
Remove-AdfsWebApiApplication [-TargetApplication] <WebApiApplication> [-PassThru] [-WhatIf] [-Confirm]
 [<CommonParameters>]
```

## 描述
`Remove-AdfsWebApiApplication` 这个 cmdlet 用于从 Active Directory Federation Services (AD FS) 中的某个应用程序中删除 Web API 应用程序角色。

## 示例

## 参数

### -PassThru
返回一个表示您正在操作的该项的对象。默认情况下，此cmdlet不会生成任何输出。

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
指定要删除的 Web API 应用程序。

```yaml
Type: WebApiApplication
Parameter Sets: ApplicationObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetIdentifier
指定要删除的 Web API 应用程序的 ID。

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
指定要删除的 Web API 应用程序的名称。

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
在运行 cmdlet 之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并未运行该cmdlet。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.IdentityServer.Management.Resources.WebApiApplication

`WebApiApplication` 对象是通过 `TargetApplication` 参数接收到的。

### System.String

字符串对象通过*TargetIdentifier*和*TargetName*参数被接收。

## 输出

### Microsoft.IdentityServer.Management.Resources.WebApiApplication

当指定 `PassThru` 参数时，该 cmdlet 会返回被移除的 `WebApiApplication` 对象。默认情况下，此 cmdlet 不会生成任何输出。

## 备注

## 相关链接

[添加 AdfsWebApi 应用程序](./Add-AdfsWebApiApplication.md)

[Get-AdfsWebApiApplication](./Get-AdfsWebApiApplication.md)

[Set-AdfsWebApiApplication](./Set-AdfsWebApiApplication.md)

