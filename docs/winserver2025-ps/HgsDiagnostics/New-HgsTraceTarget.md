---
description: 使用这个主题来帮助您通过 Windows PowerShell 管理 Windows 和 Windows Server 技术。
external help file: Microsoft.Windows.HostGuardianService.Diagnostics.Payload.dll-Help.xml
Module Name: HgsDiagnostics
ms.date: 12/20/2016
online version: https://learn.microsoft.com/powershell/module/hgsdiagnostics/new-hgstracetarget?view=windowsserver2025-ps&wt.mc_id=ps-gethelp
schema: 2.0.0
title: New-HgsTraceTarget
---

# 新的HGS跟踪目标

## 摘要
创建一个HGS诊断目标对象。

## 语法

### 远程（默认值）
```
New-HgsTraceTarget -HostName <String> [-Credential <PSCredential>] [-PSSessionConfigurationName <String>]
 [-Role <BaseHgsRoles[]>] [<CommonParameters>]
```

### NoAccess
```
New-HgsTraceTarget -HostName <String> [-NoAccess] -Role <BaseHgsRoles[]> [<CommonParameters>]
```

### 本地
```
New-HgsTraceTarget [-Local] [-Role <BaseHgsRoles[]>] [<CommonParameters>]
```

## 描述
`New-HgsTraceTarget` cmdlet 用于创建一个主机防护服务（Host Guardian Service, HGS）的诊断目标对象。`Get-HgsTrace` cmdlet 可以利用这些信息来确定如何连接到特定的主机，以及需要跟踪和诊断主机的哪些方面。

## 示例

### 示例 1：创建一个默认的目标对象
```
PS C:\> New-HgsTraceTarget -Local
```

此命令创建一个名为 `localhost` 的目标对象。由于该命令没有指定角色，因此 cmdlet 将使用当前会话的凭据，并通过目标系统上已安装的功能列表来推断相应的角色。

### 示例 2：创建一个具有不同凭据和指定角色的目标
```
PS C:\> New-HgsTraceTarget -HostName "hgs-01.contoso.com" -Credential (Get-Credential) -Role HostGuardianService
```

此命令创建一个目标对象，其主机名为 hgs-01.contoso.com，并使用提供的凭据将该目标对象设置为 HGS 节点。

### 示例 3：创建一个目标对象，使用指定的角色无法访问该目标对象
```
PS C:\> New-HgsTraceTarget -HostName "hyperv-02.contoso.com" -NoAccess -Role GuardedHost
```

此命令创建一个目标对象，其主机名为hyperv-02.contoso.com。该对象没有密码设置，但被视为受保护的宿主（即不允许未经授权的连接）。系统不会尝试连接到该“禁止访问”（NoAccess）的目标对象。

### 示例 4：创建一个目标，该目标会重用当前会话的凭据以及指定的角色
```
PS C:\> New-HgsTraceTarget -HostName "hgs-01.contoso.com" -role HostGuardianService
```

此命令创建一个目标对象，其主机名为 hgs-01.contoso.com。该目标对象会重用当前会话的凭据，并被设置为 HGS 节点。

#### 示例 5：创建一个目标，该目标重用当前会话的凭据并推断角色
```
PS C:\> New-HgsTraceTarget -HostName "hyperv-02.contoso.com"
```

此命令会创建一个目标对象，其主机名为 hyperv-02.contoso.com，并重用当前会话的凭据；随后通过目标系统上已安装的功能列表来确定该对象的角色。

## 参数

### -Credential
指定一个用于运行管理组连接的 **PSCredential** 对象。要获取一个 **PSCredential** 对象，可以使用 **Get-Credential** cmdlet。有关更多信息，请输入 `Get-Help Get-Credential`。

```yaml
Type: PSCredential
Parameter Sets: Remote
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -HostName
指定目标主机名。此参数用于在打开远程 Windows PowerShell® 会话时解析 IP 地址。

```yaml
Type: String
Parameter Sets: Remote, NoAccess
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Local
表示创建的目标是当前的本地主机。

```yaml
Type: SwitchParameter
Parameter Sets: Local
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -NoAccess
表示无法访问该目标。因此，永远不会与该目标建立连接。

```yaml
Type: SwitchParameter
Parameter Sets: NoAccess
Aliases:

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -PSSessionConfigurationName
指定在打开远程运行空间（remote runspace）时所使用的远程 Windows PowerShell 会话配置。如果省略此参数，`Get-HgsTrace` cmdlet 将使用默认的运行空间配置；或者对于具有 HostGuardianService 角色的目标对象，将使用 HGS 的默认配置。

```yaml
Type: String
Parameter Sets: Remote
Aliases:

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### -Role
指定某个目标在受保护的安全架构中所扮演的角色。该角色可以是 HGS 节点（HostGuardianService），也可以是受保护的主机（GuardedHost）。如果您未指定角色，系统将根据开放的网络连接以及所安装的 Windows 功能来推断该角色的具体类型。

```yaml
Type: BaseHgsRoles[]
Parameter Sets: Remote, Local
Aliases:
Accepted values: None, HostGuardianService, GuardedHost

Required: False
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

```yaml
Type: BaseHgsRoles[]
Parameter Sets: NoAccess
Aliases:
Accepted values: None, HostGuardianService, GuardedHost

Required: True
Position: Named
Default value: None
Accept pipeline input: False
Accept wildcard characters: False
```

### CommonParameters
此 cmdlet 支持以下常见参数：-Debug、-ErrorAction、-ErrorVariable、-InformationAction、-InformationVariable、-OutVariable、-OutBuffer、-PipelineVariable、-Verbose、-WarningAction 和 -WarningVariable。有关更多信息，请参阅关于_CommonParameters（http://go.microsoft.com/fwlink/?LinkID=113216）。

## 输入

## 输出

### Microsoft.Windows.HostGuardianService.DiagnosticsPayload.InputTarget
此 cmdlet 返回一个目标对象，该对象是一个元数据集合，其中包含了在受保护的网络环境中运行的主机操作系统的连接信息以及该主机在该网络环境中的角色。

## 备注

## 相关链接

[Test-HgsTraceTarget](./Test-HgsTraceTarget.md)

[Get-HgsTrace](./Get-HgsTrace.md)

