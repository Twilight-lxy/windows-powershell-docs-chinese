---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/stop-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Stop-AppvClientConnectionGroup
---

# Stop-AppvClientConnectionGroup

## 摘要
关闭连接组的共享虚拟环境。

## 语法

### ByGuid（默认值）
```
Stop-AppvClientConnectionGroup [-Global] [-GroupId] <Guid> [-VersionId] <Guid> [<CommonParameters>]
```

### 按名称查找
```
Stop-AppvClientConnectionGroup [-Global] [-Name] <String> [<CommonParameters>]
```

### 按连接组（ByConnectionGroup）
```
Stop-AppvClientConnectionGroup [-Global] [-ConnectionGroup] <AppvClientConnectionGroup> [<CommonParameters>]
```

## 描述
`Stop-AppvClientConnectionGroup` cmdlet 用于关闭某个连接组的共享虚拟环境。该连接组虚拟环境中所有正在运行的进程都会被终止。

## 示例

### 示例 1：停止名为某个特定组的虚拟环境
```
PS C:\> Stop-AppvClientConnectionGroup -Name "MyGroup"
```

这个命令会停止名为“MyGroup”的已启用连接组的虚拟环境。

#### 示例 2：通过使用虚拟环境的 ID 来停止某个组对应的虚拟环境
```
PS C:\> Stop-AppvClientConnectionGroup -GroupID 793afd37-bd68-4ea1-859a-669f6afd0aa8
```

此命令会停止具有组ID 793afd37-bd68-4ea1-859a-669f6afd0aa8的已启用连接组的虚拟环境。

### 示例 3：停止名称与特定字符串匹配的组的虚拟环境
```
PS C:\> Get-AppvClientConnectionGroup -Name "MyGr*" | Stop-AppvClientConnectionGroup
```

这条命令会获取所有名称中包含“MyGr”这个字符串的已启用连接组，然后停止这些连接组中的每个虚拟环境。

## 参数

### -ConnectionGroup
指定一个 App-V 连接组对象。

```yaml
Type: AppvClientConnectionGroup
Parameter Sets: ByConnectionGroup
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: True (ByValue)
Accept wildcard characters: False
```

### -Global
表示该 cmdlet 会为指定连接组中的所有用户关闭计算机上的虚拟环境。使用 *Global* 参数需要管理员权限。

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

### -GroupId
指定特定连接组的组ID。

```yaml
Type: Guid
Parameter Sets: ByGuid
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Name
指定Microsoft应用虚拟化（App-V）连接组的名称。

```yaml
Type: String
Parameter Sets: ByName
Aliases:

Required: True
Position: 0
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VersionId
指定一个 GUID，用于区分某个连接组版本与其他版本（无论是旧版本、新版本，还是属于不同分支的版本）。如果不指定此参数，该 cmdlet 将对连接组的所有版本进行操作。

```yaml
Type: Guid
Parameter Sets: ByGuid
Aliases:

Required: True
Position: 1
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutputVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [about_CommonParameters](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientConnectionGroup

## 输出

## 备注
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns an error.
* If the enable operation fails, the cmdlet returns an error.
* If the cmdlet cannot find the connection group on the target computer, the cmdlet returns an error.

## 相关链接

[Add-AppvClientConnectionGroup](./Add-AppvClientConnectionGroup.md)

[disable-AppvClientConnectionGroup](./Disable-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Mount-AppvClientConnectionGroup](./Mount-AppvClientConnectionGroup.md)

[Remove-AppvClientConnectionGroup](./Remove-AppvClientConnectionGroup.md)

[修复 AppvClientConnectionGroup](./Repair-AppvClientConnectionGroup.md)

