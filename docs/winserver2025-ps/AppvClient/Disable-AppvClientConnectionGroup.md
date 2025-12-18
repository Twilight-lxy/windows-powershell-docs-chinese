---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.AppV.AppVClientPowerShell.dll-Help.xml
Module Name: AppvClient
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/appvclient/disable-appvclientconnectiongroup?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: Disable-AppvClientConnectionGroup
---

# 禁用 AppvClientConnectionGroup

## 摘要
禁用运行App-V客户端的那台计算机上的连接组。

## 语法

### ByGuid（默认值）
```
Disable-AppvClientConnectionGroup [-Global] [-UserSID <String>] [-GroupId] <Guid> [-VersionId] <Guid>
 [<CommonParameters>]
```

### 按名称查找
```
Disable-AppvClientConnectionGroup [-Global] [-UserSID <String>] [-Name] <String> [<CommonParameters>]
```

### 按连接组（ByConnectionGroup）
```
Disable-AppvClientConnectionGroup [-Global] [-UserSID <String>] [-ConnectionGroup] <AppvClientConnectionGroup>
 [<CommonParameters>]
```

## 描述
`Disable-AppvClientConnectionGroup` cmdlet 用于禁用在运行 Microsoft 应用虚拟化（App-V）客户端计算机上已存在的连接组。

## 示例

#### 示例 1：通过使用连接组的名称来禁用该连接组
```
PS C:\> Disable-AppvClientConnectionGroup -Name "MyGroup"
```

此命令会禁用名为“MyGroup”的连接组。

### 示例 2：通过使用连接组的ID来禁用该连接组
```
PS C:\> Disable-AppvClientConnectionGroup -GroupID 35ec9e5f-ab21-463f-8fe6-b90d4b66d182
```

此命令将禁用组ID为35ec9e5f-ab21-463f-8fe6-b90d4b66d182的连接组。

### 示例 3：禁用所有名称与指定字符串匹配的连接组
```
PS C:\> Get-AppvClientConnectionGroup -Name "MyGr*" | Disable-AppvClientConnectionGroup
```

这个命令会获取所有名称中包含“MyGr”字符串的连接组，然后将其禁用。

## 参数

### -ConnectionGroup
指定一个App-V连接组对象。

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
表示此 cmdlet 会禁用所有登录目标计算机的用户的连接组；否则，它只会禁用当前正在运行的用户的连接组。

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
指定与特定连接组关联的 GUID。

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
指定 App-V 连接组的名称。

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

### -UserSID
指定目标用户的 SID，格式为 S-1-2-34-56789012-3456789012-345678901-2345。运行此参数需要具有提升的权限。

```yaml
Type: String
Parameter Sets: (All)
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -VersionId
指定一个 GUID，用于区分该连接组版本与其他版本。如果您不指定此参数，该 cmdlet 将对所有版本的连接组进行操作。

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
此 cmdlet 支持以下常用参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅 [关于通用参数](https://go.microsoft.com/fwlink/?LinkID=113216)。

## 输入

### Microsoft.AppvAgent.AppvClientConnectionGroup

## 输出

## 备注
* The cmdlet checks that you have permissions to perform the specific action. If not, the cmdlet returns the following error: The action could not be performed due to current App-V permissions. Please modify the permissions and try the operation again.
* If the disable operation fails, the cmdlet returns the following error: The disable operation could not be completed. An error code is returned.
* If any package in the specified group is running, the connection group will not be disabled until all packages in the new group are shutdown. The cmdlet will still return success as long as the file is valid.
* If the cmdlet cannot find the connection group, the cmdlet returns the following error: The specified connection group could not be found on the target system.

## 相关链接

[Add-AppvClientConnectionGroup](./Add-AppvClientConnectionGroup.md)

[Enable-AppvClientConnectionGroup](./Enable-AppvClientConnectionGroup.md)

[Get-AppvClientConnectionGroup](./Get-AppvClientConnectionGroup.md)

[Mount-AppvClientConnectionGroup](./Mount-AppvClientConnectionGroup.md)

[Remove-AppvClientConnectionGroup](./Remove-AppvClientConnectionGroup.md)

[修复 AppvClientConnectionGroup](./Repair-AppvClientConnectionGroup.md)

[Stop-AppvClientConnectionGroup](./Stop-AppvClientConnectionGroup.md)

