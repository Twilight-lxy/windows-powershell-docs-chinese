---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: AssignedAccess-help.xml
Module Name: AssignedAccess
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/assignedaccess/set-assignedaccess?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Set-AssignedAccess
---

# 设置分配的访问权限

## 摘要
配置用户仅能启动一个应用程序。

## 语法

### UserName ANDAppName（默认值）
```
Set-AssignedAccess -UserName <String> -AppName <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UserName AND AppId
```
Set-AssignedAccess -UserName <String> -AppUserModelId <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UserSid AND AppId
```
Set-AssignedAccess -UserSID <String> -AppUserModelId <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

### UserSidANDAppName
```
Set-AssignedAccess -UserSID <String> -AppName <String> [-WhatIf] [-Confirm] [<CommonParameters>]
```

## 描述
`Set-AssignedAccess` cmdlet 用于配置指定的用户账户，使其只能使用一个 Windows 应用程序。该用户无法退出该应用程序、登出系统或访问任何系统设置。

如果用户已登录，或者计算机配备了 PS/2 键盘，那么你必须重新启动计算机才能使更改生效。

要退出已分配的访问权限，请快速按五下左侧的Windows图标键。

“分配访问权限”（Assigned Access）相关的cmdlet仅支持Windows 10和Windows 11客户端操作系统。

## 示例

### 示例 1：根据 SID 和应用程序名称设置分配的访问权限
```
PS C:\> Set-AssignedAccess -UserSID "S-1-5-21-523423449-2432423479-234123443-1004" -AppName "CustomApp"
```

该命令通过使用用户SID（安全标识符）和应用程序名称来配置分配的访问权限。

### 示例 2：根据用户名和 AppUserModelID 设置分配的访问权限
```
PS C:\> Set-AssignedAccess -UserName "UserName" -AppUserModelId "microsoft.windowsphotos_8wekyb3d8bbwe!app"
```

此命令通过使用用户名和AppUserModelID来配置指定的访问权限。

## 参数

### -AppName
指定用于分配访问权限的已安装 Windows 应用商店应用程序的名称。支持使用通配符字符。

```yaml
Type: String
Parameter Sets: UserNameANDAppName, UserSidANDAppName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -AppUserModelId
指定已安装的 Windows Store 应用程序用于分配访问权限的应用程序用户模型 ID（AppUserModelID）。该 ID 可以在应用程序的 AUMIDs.txt 文件中找到。

```yaml
Type: String
Parameter Sets: UserNameANDAppId, UserSidANDAppId
Aliases: AUMID

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Confirm
在运行 cmdlet 之前会提示您进行确认。

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

### -UserName
指定用于分配访问权限的本地用户账户名称。该账户不能是域账户或管理员账户。

```yaml
Type: String
Parameter Sets: UserNameANDAppName, UserNameANDAppId
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -UserSID
指定用于分配访问权限的本地用户账户的安全标识符（SID）。该账户不能是域账户或管理员账户。

```yaml
Type: String
Parameter Sets: UserSidANDAppId, UserSidANDAppName
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -WhatIf
展示了如果该cmdlet被运行会发生什么情况。但实际上该cmdlet并没有被运行。

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

### 没有（需要处理的内容）。
您不能将输入数据通过管道传递给这个cmdlet。

## 输出

### System.Object

## 备注
* To get all the Windows Store apps installed for a user account, use the Get-AppxPackage cmdlet as follows:

`Get-AppxPackage -User "username"`

## 相关链接

[Clear-AssignedAccess](./Clear-AssignedAccess.md)

[获取分配的访问权限](./Get-AssignedAccess.md)

