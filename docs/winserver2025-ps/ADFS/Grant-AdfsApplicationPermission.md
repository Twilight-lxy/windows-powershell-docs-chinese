---
description: 使用这个主题来借助 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.IdentityServer.Management.dll-Help.xml
Module Name: ADFS
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/adfs/grant-adfsapplicationpermission?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Grant-AdfsApplicationPermission
---

# 授予 AdFS 应用程序权限

## 摘要
允许提交资助申请。

## 语法

### ClientRoleIdentifier（默认值）
```
Grant-AdfsApplicationPermission [-ClientRoleIdentifier] <String> [-ServerRoleIdentifier] <String>
 [[-ScopeNames] <String[]>] [-Description <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

### 允许所有已注册的客户访问
```
Grant-AdfsApplicationPermission [-AllowAllRegisteredClients] [-ServerRoleIdentifier] <String>
 [[-ScopeNames] <String[]>] [-Description <String>] [-PassThru] [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Grant-AdfsApplicationPermission` cmdlet 可在 Active Directory Federation Services (AD FS) 中授予应用程序相应的权限。

## 示例

## 参数

### -AllowAllRegisteredClients
用于指示是否允许所有已注册的客户访问。

```yaml
Type: SwitchParameter
Parameter Sets: PermitAllRegisteredClients
Aliases:
Accepted values: true

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ClientRoleIdentifier
指定一个客户端角色标识符。

```yaml
Type: String
Parameter Sets: ClientRoleIdentifier
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Description
指定一个描述信息。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

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

### -ScopeNames
指定一个范围名称数组。

```yaml
Type: String[]
Parameter Sets: (All)
Aliases:

Required: False
Position: 2
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -ServerRoleIdentifier
指定一个服务器角色标识符。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: True (ByPropertyName)
Accept wildcard characters: False
```

### -Confirm
在运行该cmdlet之前，会提示您进行确认。

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
展示了如果运行该cmdlet会发生什么情况。但实际上并没有运行该cmdlet。

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

### System.ManagementAutomation.SwitchParameter

`SwitchParameter` 对象是通过 `AllowAllRegisteredClients` 参数接收到的。

### System.String

字符串对象通过 *ClientRoleIdentifier*、*Description*、*ScopeNames* 和 *ServerRoleIdentifier* 参数被接收。

## 输出

### Microsoft.IdentityServer.Management.Resources.OAuthPermission

当指定 `PassThru` 参数时，会返回一个新的 `OAuthPermission` 对象。默认情况下，此 cmdlet 不会产生任何输出。

## 备注

## 相关链接

[Get-AdfsApplicationPermission](./Get-AdfsApplicationPermission.md)

[Revoke-AdfsApplicationPermission](./Revoke-AdfsApplicationPermission.md)

[Set-AdfsApplicationPermission](./Set-AdfsApplicationPermission.md)

