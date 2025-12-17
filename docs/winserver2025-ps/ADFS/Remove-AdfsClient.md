---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/remove-adfsclient?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Remove-AdfsClient
---

# 移除 AdFS 客户端

## 摘要
删除当前在 AD FS 中注册的 OAuth 2.0 客户端的注册信息。

## 语法

### 名称（默认值）
```
Remove-AdfsClient [-TargetName] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### ClientId
```
Remove-AdfsClient [-TargetClientId] <String> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### InputObject
```
Remove-AdfsClient [-TargetClient] <AdfsClient> [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Remove-AdfsClient` cmdlet 用于删除当前在 Active Directory Federation Services (AD FS) 中注册的 OAuth 2.0 客户端的注册信息。删除该客户端的注册信息后，AD FS 将不再向该客户端颁发授权码或访问令牌。

## 示例

#### 示例 1：删除 OAuth 客户端的注册信息
```
PS C:\> Remove-AdfsClient -TargetName "Payroll Application"
```

此命令会删除名为“Payroll Application”的OAuth 2.0客户端的注册信息。

## 参数

### -PassThru
返回一个表示您正在操作的项的对象。默认情况下，此cmdlet不会生成任何输出。

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

### -TargetClient
指定要删除的已注册的 OAuth 2.0 客户端。

```yaml
Type: AdfsClient
Parameter Sets: InputObject
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -TargetClientId
用于指定要删除的已注册的 OAuth 2.0 客户端的客户端标识符。

```yaml
Type: String
Parameter Sets: ClientId
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -TargetName
指定要删除的已注册的 OAuth 2.0 客户端的名称。

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
此cmdlet支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft IdentityServer.Management.Resources.AdfsClient

`AdfsClient` 对象是通过 `*TargetClient*` 参数接收到的。

### System.String

字符串对象通过 *TargetClientId* 和 *TargetName* 参数被接收。

## 输出

### Microsoft IdentityServer.Management.Resources.AdfsClient

当指定*PassThru*参数时，该命令会返回被删除的AdfsClient对象。默认情况下，此Cmdlet不会生成任何输出。

## 备注

## 相关链接

[Add-AdfsClient](./Add-AdfsClient.md)

[禁用 AdfsClient](./Disable-AdfsClient.md)

[Enable-AdfsClient](./Enable-AdfsClient.md)

[Get-AdfsClient](./Get-AdfsClient.md)

[Set-AdfsClient](./Set-AdfsClient.md)

